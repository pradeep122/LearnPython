class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        # print("Talk...")
        print(f"Hi I'm {self.name}")


person1 = Person("Nirvaan")
# print(person1.name)
person1.talk()
