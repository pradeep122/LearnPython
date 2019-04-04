# A constructor is a function that gets
# called at the time of creating an object


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move..")

    def draw(self):
        print("Draw..")


point = Point(10, 20)
print(point.x)
