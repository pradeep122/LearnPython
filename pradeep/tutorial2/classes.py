# Types in Python

# Simple Types
# --------
# Numbers
# Strings
# Booleans

# Complex Types
# --------
# Lists
# Tuples
# Dictionaries

# Custom Types
# --------
# Classes


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


# point1 = Point()
# Class attributes can be added to an object anywhere in the program
# and not necessarily in the class
# point1.x = 10
# point1.y = 10

point1 = Point(10, 20)
point1.draw()
point1.move()
print(f'({point1.x}, {point1.y})')


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'My name is {self.name}')


person = Person('Pradeep')
person.talk()


class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def meow(self):
        print('Meow!')


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.meow()
