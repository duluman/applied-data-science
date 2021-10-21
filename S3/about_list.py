"""
List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
"""

cubes = [i**3 for i in range(7)]

print(cubes)

odd_list = [i * 2 + 3 for i in range(1, 11)]

print(odd_list)

"""
A list comprehension can also contain an if statement to enforce a condition on values in the list.
"""
evens = [i**2 for i in range(17) if i**2 % 2 == 0]

print(evens)