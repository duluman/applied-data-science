"""
Sets are similar to lists or dictionaries.
They are created using curly braces, and are unordered, which means that they can't be indexed.
-- Sets cannot contain duplicate elements. --
Due to the way they're stored, it's faster to check whether an item is part of a set using the in operator,
rather than part of a list.
"""


nums = {1, 7, 1, 3, 1, 3, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

"""
You can use: 
- add() function to add new items to the set
- remove() to delete a specific element
"""

"""
Sets can be combined using mathematical operations.


"""

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

# The union operator | combines two sets to form a new one containing items in either.
print(first | second)

# The intersection operator & gets items only in both.
print(first & second)

# The difference operator - gets items in the first set but not in the second.
print(first - second)
print(second - first)

# The symmetric difference operator ^ gets items in either set, but not both.
print(first ^ second)