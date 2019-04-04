# Parameters are the placeholders which
# is used in function to receive information

# Arguments are the actual value
#  given to the placeholder of a function


def greet_user(name):  # name is a parameter
    print(f"Hi {name}!")
    print("Welcome aboard")


print("start..")
greet_user("Nirvaan")
greet_user("Pradeep")
print("Finish..")

# If we didn't pass an argument to a function
# TypeError: greet_user() missing 1 required positional argument: 'name'
# greet_user()


# For Multiple Parameters:

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Begin")
# These are known as positional arguments
# passing correct arguments to the parameters
greet_user("vijayalakshmi", "Kalidindi")
print("Done")
