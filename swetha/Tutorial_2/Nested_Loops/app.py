# If we want to generate coordinates then we use nested loops
# (x,y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# EXERCISE

# XXXXX
# XX
# XXXXX
# XX
# XX

# Without using nested for loops
# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     print("x" * number)

# Using Nested For Loops

# count = 6
# name = " "
# for i in range(count):
#     name += 'x'
# print(name)

numbers = [5, 2, 5, 2, 2]

for number in numbers:
    x_label = ""
    for i in range(number):
        x_label += 'x'
    print(x_label)
