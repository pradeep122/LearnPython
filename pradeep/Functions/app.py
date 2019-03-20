# Functions in Python
def greet():
    print("Hi there")
    print("Welcome Aboard")


greet()

# Functions with arguments


def greet_name(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet_name("Pradeep", "Dantuluri")


# Functions with return values
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Pradeep")
print(message)

file = open("contents.txt", "w")
file.write(message)

# Keyword Arguments


def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, by=2))

# Tuple arguments


def multiply(*numbers):
    total = 1
    for number in numbers:
        print(number)
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# Dictionary Arguments


def save_user(**user):
    print(user["name"])


save_user(id=1, name="Pradeep", age=33)
