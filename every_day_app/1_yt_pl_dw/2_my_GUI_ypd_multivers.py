# Importing necessary packages
import datetime
import random
import tkinter as tk
from tkinter import *
from pytube import *
from tkinter import messagebox, filedialog
from datetime import date

def Widgets():
    head_label = Label(root, text="YouTube Playlist Video Downloader Using Tkinter",
                    padx=15,
                    pady=15,
                    font="SegoeUI 16",
                    bg="white",
                    fg="red")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)

    link_label = Label(root,
                    text="YouTube playlist link :",
                    bg="red",
                    pady=5,
                    padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                        width=35,
                        textvariable=video_Link,
                        font="Arial 14")
    root.linkText.grid(row=2,
                    column=1,
                    pady=5,
                    padx=5,
                    columnspan=2)


    destination_label = Label(root,
                            text="Destination :",
                            bg="red",
                            pady=5,
                            padx=9)
    destination_label.grid(row=3,
                        column=0,
                        pady=5,
                        padx=5)


    root.destinationText = Entry(root,
                                width=27,
                                textvariable=download_Path,
                                font="Arial 14")
    root.destinationText.grid(row=3,
                            column=1,
                            pady=5,
                            padx=5)


    browse_B = Button(root,
                    text="Browse",
                    command=Browse,
                    width=10,
                    bg="bisque",
                    relief=GROOVE)
    browse_B.grid(row=3,
                column=2,
                pady=1,
                padx=1)

    Download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)

def Browse():

    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")

    download_Path.set(download_Directory)


def Download():

    # getting user-input Youtube Link
    Youtube_link = video_Link.get()
    playlist = Playlist(Youtube_link)

    # select the optimal location for
    # saving file's
    try:

        today_day = date.today()
        today_ms = f"{datetime.datetime.now().minute}m {datetime.datetime.now().second}s"
        today_folder_name = today_day.strftime("%m-%B-%d-%Y")
        play_list_name = playlist.title
        clear_playlist_name = today_folder_name + "_yt_dw_" + re.sub('[^a-zA-Z\s]+', '', play_list_name) + f"{today_ms}"
    except:

        clear_playlist_name = Youtube_link.lstrip("https://www.youtube.com/playlist?list=")

    download_Folder = download_Path.get() + "/" + clear_playlist_name
    number_of_video = 1

    for video in playlist.videos:
        try:
            # print(video.streams.filter(file_extension='mp4'))
            stream = video.streams.get_by_itag(299)  # 37 = 1080p audio+video
            stream.download(output_path=download_Folder, filename_prefix=str(number_of_video) + " - 1080 no sound")
            print("1080")
            try:
                file_write = open(f"{download_Folder}\\#readme_playlist.txt", "a")
                file_write.write("\n")
                file_write.write(f"Number of video is {number_of_video} \n")
                file_write.write(f"The author of the {video.title} is {video.author}. \n")
                # file_write.write(f"The link of the video: {video.embed_url} \n")
                # file_write.write(f"Number of views {video.views} since {video.initial_data}. \n")
                file_write.write("- - " * 7)
                file_write.write("\n")
                file_write.close()

            except:
                print("We could not update details of the video in the readme file")

            finally:
                stream = video.streams.get_by_itag(22)  # 22 = 720p audio+video
                stream.download(output_path=download_Folder, filename_prefix=str(number_of_video) + " - 720 finally ")


        except AttributeError:

            try:
                stream = video.streams.get_by_itag(22)  # 22 = 720p audio+video
                stream.download(output_path=download_Folder, filename_prefix=str(number_of_video) + " - 720 ")
                print("720")
                try:
                    file_write = open(f"{download_Folder}\\#readme_playlist.txt", "a")
                    file_write.write("\n")
                    file_write.write(f"Number of video {number_of_video} \n")
                    file_write.write(f"Author of the {video.title} . \n")
                    # file_write.write(f"The link of the video: {video.embed_url} \n")
                    # file_write.write(f"Number of views {video.views} since {video.initial_data}. \n")
                    file_write.write("- - " * 7)
                    file_write.write("\n")
                    file_write.close()

                except:
                    print("We could not update details of the video in the readme file")
            except:
                stream = video.streams.get_by_itag(18)  # 18 = 360p audio+video
                stream.download(output_path=download_Folder, filename_prefix=str(number_of_video) + " - 360 ")
                print("360")

        except:
            print("Something went wrong.")

        print(f" \t Video number is: {number_of_video} \n")

        number_of_video += 1
    print("Final of the loop")


    try:
        file_write = open(f"{download_Folder}\\#readme_playlist.txt", "a")
        file_write.write("- - " * 7)
        file_write.write(f"You have {number_of_video} files downloaded from: {Youtube_link} \n")
        file_write.write(f"The playlist ID is {Youtube_link.lstrip('https://www.youtube.com/playlist?list=')} \n")
        file_write.write(f"Date is: {date.today()}")
        file_write.write("\n")
        file_write.close()

    except:
        print("We could not creat the readme file")

    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)

root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("720x320")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="#49A")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

Widgets()
print("Before final")
# Defining infinite loop to run application
root.mainloop()

print("Final")