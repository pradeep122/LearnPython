# Functions are of two types
# 1. Performs a task eg: print()
# 2. returns a value eg: round(1.9)
# All functions return NONE by default if we did not return it

# Every time we have to write this function


def greet(name):
    print(f"Hi {name}")


print(greet("swetha"))


# This function can be reused
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Swetha")
file = open("content.txt", "w")
file.write(message)
