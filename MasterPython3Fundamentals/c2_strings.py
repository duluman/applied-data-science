"""
WRITE A CODE THAT PROMPTS A USER REQUESTING HIS/HER E-MAIL AND THEN EXTRACTS THE USERNAME
(NOTE THAT THE EMAIL IS IN FIRSTNAME.LASTNAME@GMAIL.COM
"""

message = input("Tell me your email address, please! \n \t")

user_name = message.split("@")[0]

print(f"Your username is {user_name}")

"""
WRITE A CODE THAT TAKES THE USER E-MAIL AND COUNTS THE NUMBER OF USERNAME CHARACTERS
"""

print(f"Your username has {len(user_name)} characters.")
