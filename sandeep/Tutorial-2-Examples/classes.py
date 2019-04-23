# The convention we use for naming our classes is different from naming variables and functions
# In functions and variables we always use lower case letter and _ to seperate words but in
# classes we don't use _ to seperate multiple words instead we use capital letter in the starting of a word.
# example class Point or class EmailClient


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
