# SCOPE which refers a region of the code where the variable is declared


def greet(name):
    message = "a"
    return message


print(greet("swetha"))

# name is a local variable# to that function so it throws an error


def greet(name):
    message = "b"  # message is a local variable
    print(name)


greet("swetha")

message = "b"  # "message" is a global variable


def greet(name):
    message = "a"  # "message" is a local variable
    print(name)  # "name" is a local variable


greet("nirvaan")
