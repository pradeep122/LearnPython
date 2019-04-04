import random

# My Solution


class Dice:
    def roll(self):
        numbers = (1, 2, 3, 4, 5, 6)
        x = random.choice(numbers)
        y = random.choice(numbers)
        return x, y


dice1 = Dice()
print(dice1.roll())

# Solution
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second


# dice = Dice()
# print(dice.roll())
