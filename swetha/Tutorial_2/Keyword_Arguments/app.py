# Keyword Argument is combination of having the parameter name
# followed by its value is a key word argument
# With Keyword argument the position doesn't really matter.


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start..")

# For most part use positional arguments
greet_user("pradeep", "Dantuluri")
greet_user(last_name="Dantuluri", first_name="Aadhya")

# If we're dealing with functions which takes multiple numerical values
# use keyword arguments to improve the readability of the code

# calc_cost(total=50, shipping=5, discount=0) -> keyword arguments

# Finally if we are passing both positional and keyword arguments
# use the keyword argument after the positional argument
greet_user("Nirvaan", last_name="Dantuluri")

# If we pass keyword arguments before positional
# we get SyntaxError: positional argument follows keyword argument
# greet_user(first_name="Sowmya", "Dantuluri")

# TypeError: greet_user() got multiple values for argument 'first_name'
# greet_user("Dantuluri", first_name="Sowmya")

print("Finish..")
