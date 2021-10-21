"""
Data Structures

Python supports the following collection types: Lists, Dictionaries, Tuples, Sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot/should not change.
Many times, a tuple is used in combination with a dictionary, for example,
a tuple might represent a key, because it's immutable.
"""

"""
Given a string as input, you need to output how many times each letter appears in the string.
You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
Create a program to take a string as input and output a dictionary, which represents the letter count.

"""

text = input()
dict = {}


for leter in text:
    if leter not in dict:
        dict[leter] = 1
    else:
        dict[leter] += 1

print(dict)