import random

guessing_number = int(input("Tell me a number between 1 and 49: \n \t"))

random_number = random.randint(1, 49)

print(" * -" * 7)

while True:

    if random_number == guessing_number:
        print(" # _ / - " * 3)
        print("Yey!!!! \n You have the right number!!!")
        print(" # _ / - " * 3)
        break
    elif random_number < guessing_number:
        print("Your guess is high")
        guessing_number = int(input("Try again: \n \t"))

    else:
        print("Your guess is lower")
        guessing_number = int(input("Try again \n \t"))

    print(" * -" * 7)