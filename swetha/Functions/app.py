# Custom Functions
# we have to define the function and then add the function name
# function name should be in lower case
# function name should be separated with underscore


def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


def increment(number, by):
    return number + by


# result = increment(2, 1)
# print(result)
print(increment(2, by=1))


def increment(number, by=1):
    return number + by


print(increment(2))


def increment(number, by=1):
    return number + by


print(increment(2, 5))
