# For Loop is used to iterate over items of a collection such as string
# for string
for item in 'Python':
    print(item)
# P
# y
# t
# h
# o
# n

# for array or list of names
for item in ['Swetha', 'Pradeep', 'Nirvaan']:
    print(item)
# Swetha
# Pradeep
# Nirvaan

# for list of numbers
for item in [1, 2, 3, 4]:
    print(item)
# 1
# 2
# 3
# 4

# Range is an object used to iterate range of numbers
for item in range(10):
    print(item)

# range between 5 to 10
for item in range(5, 10):
    print(item)

# we can also give a stem in range function
for item in range(5, 10, 2):
    print(item)


# EXERCISE

prices = [10, 20, 30]
total = 0
for price in prices:
    total = total + price
print(f"Shopping cart: {total}")
