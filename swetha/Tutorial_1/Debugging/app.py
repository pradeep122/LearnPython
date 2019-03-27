def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))


def multiply_even(*numbers):
    total = 1
    for number in numbers:
        if number % 2 == 0:
            total *= number

    return total


print(multiply_even(1, -2, 3, 4))
