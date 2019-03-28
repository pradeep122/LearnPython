def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)
# Use [] - for lists
# Use () -  for tuples (similar to list but cannot modify the collection)


def multi(*num):
    for number in num:
        print(number)


multi(1, 3, 5, 7)
