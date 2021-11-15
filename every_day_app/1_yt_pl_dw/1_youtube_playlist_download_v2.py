
"""
https://pytube.io/en/latest/index.html
pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.
https://gist.github.com/sidneys/7095afe4da4ae58694d128b1034e01e2
YouTube video stream format codes
37 	mp4 	audio/video 	1080p
22 	mp4 	audio/video 	720p
"""
from datetime import *
from pytube import Playlist

url_playlist = "https://www.youtube.com/watch?v="

today_now = date.today()

today_folder_name = today_now.strftime("%m-%B-%d-%Y")

playlist = Playlist(url_playlist)
# print(f'Number of videos in playlist:{len(playlist)}')
clear_playlist_name = url_playlist.lstrip("https://www.youtube.com/playlist?list=")
today_ms = f"{datetime.now().minute}m {datetime.now().second}s"
download_directory = f"D:\yTube\#python_download\{today_folder_name} {today_ms}"
# Loop through all videos in the playlist and download them
number_of_video = 1

for video in playlist.videos:
    try:
        # print(video.streams.filter(file_extension='mp4'))
        # stream = video.streams.get_by_itag(299)  # 37 = 1080p audio+video
        # stream.download(output_path=download_directory, filename_prefix=str(number_of_video)+"- 1080 ")
        # print("1080")
        stream2 = video.streams.get_by_itag(22)  # 22 = 720p audio+video
        stream2.download(output_path=download_directory, filename_prefix=str(number_of_video) + "-  720 ")
        file_write = open(f"{download_directory}\\#readme_playlist_v2.txt", "a")
        file_write.write("- - " * 7)
        file_write.write("\n")
        file_write.write(f"\n {number_of_video} - {video.title} \n")
        file_write.write(f"The number of views: {video.views} since the beginning until {today_folder_name} \n ")
        file_write.write("- - " * 7)
        file_write.write("\n \n")
        file_write.close()

    # except AttributeError:
    #     stream = video.streams.get_by_itag(22)  # 22 = 720p audio+video
    #     stream.download(output_path=download_directory, filename_prefix=str(number_of_video)+"- 720 ")
    #     print("720")

    except:
        print("Something went wrong.")
        continue

    print(f" \t Video number is: {number_of_video} \n")

    number_of_video += 1

count_url_video = 1

for url1 in playlist.video_urls:
    try:
        file_write = open(f"{download_directory}\\#readme_playlist.txt", "a")
        file_write.write("- - " * 7)
        file_write.write(f"\n{count_url_video} - {number_of_video} You have downloaded from: {url1} \n")
        file_write.write(f"The playlist ID is {url1.lstrip('https://www.youtube.com/playlist?list=')} \n")
        file_write.write(f"Date is: {date.today()}")
        file_write.write(f"{clear_playlist_name}\n")
        file_write.close()
        count_url_video += 1

    except:
        print("We could not creat the readme file")
        continue

# number_of_audio = 0
# for video in playlist.videos:
#     try:
#         print(video.streams.filter(file_extension='mp4'))
#
#         # audio_file = video.streams.get_audio_only("mp3")
#         audio_file = video.streams.filter(res="1080p", file_extension='mp4').first()
#         audio_file.download(output_path=download_directory, filename_prefix=str(number_of_audio)+ " ")
#
#     except:
#         print("Something went wrong.")
#
#     number_of_audio += 1
#
#     print(f" \t Audio number is: {number_of_audio} \n")