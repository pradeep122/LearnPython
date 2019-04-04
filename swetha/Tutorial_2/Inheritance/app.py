# Inheritance is the process of extends or inheriting
# the properties from parent/super class to child/base class

# Acquiring the behavior or attributes from the parent class to child class


class Mammal:
    def walk(self):
        print("Walk...")

# Dog class Extending Mammal class


class Dog(Mammal):
    def bark(self):
        print("Bark...")


# Cat class inheriting Mammal class
class Cat(Mammal):
    def be_annoyed(self):
        print("Annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoyed()

mammal1 = Mammal()
mammal1.walk()
