# Inheritance is a mechanism of reusing the code
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass  # To the pass the line


dog1 = Dog()
dog1.walk()
