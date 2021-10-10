
print(" - " * 7)  # -  -  -  -  -  -  -

for i, element in enumerate('mangos'):
    print(i, element)

"""
OUTPUT:
0 m
1 a
2 n
3 g
4 o
5 s
"""

print(" - " * 7)  # -  -  -  -  -  -  -

for x in range(1, 3):  # slow loop
    for y in range(1, 7):   # fast loop
        print('{} * {} = {}'.format(x, y, x*y))

print(" - " * 7)  # -  -  -  -  -  -  -

color_list = ['black', 'white', 'gold']  # slow loop
phone_list = ['iphone', 'samsung', 'blackberry']  # fast loop

for i in color_list:
    for j in phone_list:
        print(i, j)

print(" - " * 7)  # -  -  -  -  -  -  -

for i in reversed(range(7)):
    print(i)