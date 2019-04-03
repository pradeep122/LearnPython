# We use classes to define new types to model real concepts.
# We use "Pascal Naming Convention" for classes i.e;
# We capitalize the first letter of every word.
# we don't separate the words with underscore
# as we do it to variables and functions.

# Class is a blueprint or template for creating an object.
# Object is an instance of class.
# Classes can have methods which are defined in the body of the class.
# classes have attributes we can set anywhere in the programs.


class Point:
    def move(self):
        print("Move..")

    def draw(self):
        print("Draw..")


point1 = Point()
point1.draw()
# We are assigning attributes to the object
point1.x = 10
point1.y = 20
print(point1.x)  # 10
point1.move()

# We are creating another object to Point class
point2 = Point()

# If we won't have an attribute and print then we get
# AttributeError: 'Point' object has no attribute 'x'
# print(point2.x)

point2.x = 1
print(point2.x)
