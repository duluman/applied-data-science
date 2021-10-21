"""
The built-in functions map and filter are very useful higher-order functions that operate on lists
(or similar objects called iterables).
The function map takes a function and an iterable as arguments,
and returns a new iterable with the function applied to each argument.
"""


def add_five(x):
    return x + 5


nums = [14, 26, 31, 47, 55]
#  To convert the result into a list, we used list explicitly.
result = list(map(add_five, nums))
print(result)


def make_string(x):
    return str(x) + " Nice"


string_list = list(map(make_string, nums))
print(string_list)

double_list = list(map(lambda x: x * 2, nums))

print(double_list)


"""
The function filter filters an iterable by leaving only the items that match a condition (also called a predicate).
Like map, the result has to be explicitly converted to a list if you want to print it.
"""


lista_filtrata = list(filter(lambda x: x % 2 == 0, nums))
print(lista_filtrata)

lista_filtrata2 = list(filter(lambda x: x > 27, nums))
print(lista_filtrata2)