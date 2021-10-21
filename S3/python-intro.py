

class Person():

    def __init__(self):
        self.name = ""
        self.age = ""

    def display_person(self):
        print(f"My name is {self.name} and I have {self.age} years old.")


person1 = Person()
person1.name = 'Cristian'
person1.age = 32

person1.display_person()

a = 1
b = 2

print(a <= b)

while True:
    print('infinit')