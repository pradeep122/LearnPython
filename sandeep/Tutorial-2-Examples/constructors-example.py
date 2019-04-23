class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


sandeep = Person("Sandeep D")
print(sandeep.name)
sandeep.talk()

pradeep = Person("Pradeep D")
pradeep.talk()
