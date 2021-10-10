"""
Given a string, write a python function to check if it is palindrome or not.
A string is said to be palindrome if the reverse of the string is the same as string.
For example, “radar” is a palindrome, but “radix” is not a palindrome.
"""

# mesaj = input()


# def palindrome(x):
#     if x == x[::-1]:
#         print("True")
#         return True
#
# a = palindrome(mesaj)

# ------------------------

def palindrome3(x):
    b = x[::-1]
    if x == b:
        print(f' {x} is a palindrome.')
        return True
    else:
        print(f' {x} is not a palindrome.')
        return False


mesaj2 = 'radar'
c = palindrome3(mesaj2)

mesaj3 = 'castane'
d = palindrome3(mesaj3)


# ------------------------

x = 'radar'


def palindrom(p):

    y = ""
    for i in range(0, len(p)):
        y += p[len(p)-i-1]
    if y == p:
        return True
    else:
        return "Nu E"


print(palindrom(x))

# ------------------------
