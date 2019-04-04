
class Dice:
    def roll(self):
        import random
        return random.randint(1, 6), random.randint(1, 6)


if __name__ == "__main__":
    print(Dice().roll())
