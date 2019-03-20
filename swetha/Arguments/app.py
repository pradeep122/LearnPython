# PARAMETERS are those that we pass it to the function
# whereas ARGUMENTS are the actual values
# we pass it when calling the function


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")


greet("Vijayalakshmi", "Kalidindi")
greet("Nirvaan", "Dantuluri")


def multiply(x, y):
    return x * y


print(multiply(4, 5))


def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)


def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 3, 4, 5))


# ** is used to add the key value pairs or keyword aruments to the function

def save_user(**user):
    print(user)


save_user(id=1, name="swetha", age=27)


def save_user(**user):
    print(user["age"])


save_user(id=2, name="nirvaan", age="7 months")
