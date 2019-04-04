# Function is a container which is used
# to store small chunks of code and
# can be reused

# We have to define the function first
# After that we need to call the function

# If we call the function before defining we will get error
# greet_user()  # NameError: name "greet_user" is not defined


def greet_user():
    print("Hi there")
    print("Welcome Aboard!")


print("Start...")
greet_user()
print("Finish...")
