#  while loops

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1

print('Done')

# For Loops

# Looping over characters of a string

print(' ---- Looping over characters of a string')
for item in 'Python':
    print(item)

# Looping over strings in an array
print(' ---- Looping over strings in an array')
for item in ['Pradeep', 'Varma', 'Dantuluri']:
    print(item)

# Looping over integers in an array
print(' ---- Looping over integers in an array')
for item in [1, 2, 3, 4]:
    print(item)

# Looping over a range of integers
print(' ---- Looping over a range of integers')
for item in range(5, 10):
    print(item)

# Looping over a range with stop
print(' ---- Looping over a range with stop')
for item in range(5, 10, 2):
    print(item)


# Total price of a shopping cart
prices = [10, 20, 30]
sum = 0

for price in prices:
    sum += price

print(f"Total price of Shopping cart - {sum}")


# Nested For Loops
print(' ---- Nested For Loops')
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


# Print 7 with nested For Loops
print(' ---- Print 7 with nested For Loops')
numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     print('X' * number)

for number in numbers:
    x_label = ''
    for length in range(number):
        x_label += 'X'
    print(x_label)
