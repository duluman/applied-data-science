"""

Given a strig, return the sting with the words in alphabetical order

"""


def sort_string(message):
    # we create a list from the string
    created_list = message.split()
    # we create an empty list because the order method puts capital letter firs
    edit_list = []
    # we put the word in lower case in front of the initial word the list
    for word in created_list:

        edit_list.append(word.lower() + word)
    # we sort the new list
    edit_list.sort()
    # we initialize a new list to add the original word in it
    order_list = []
    for word in edit_list:
        first_index = len(word) // 2
        order_list.append(word[first_index:])
    # we create a string with the new words
    message_in_order = ' '.join(order_list)

    return message_in_order


print(sort_string("I am Cristian and I learn Python"))
