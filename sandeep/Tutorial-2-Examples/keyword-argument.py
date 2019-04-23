# If we use keyword arguments position of the arguments does not matter in functions


def greet_users(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome Aboard')


# Below examples are of positional arguments.
# Positional arguments are default
greet_users("Sandeep", "D")
greet_users("D", "Pradeep")
# If keyword arguments are used position does not matter
# ***** Keyword arguments should always come after Positinal arguments *****
greet_users(last_name="D", first_name="Pradeep")
# calc_cost(total=50, shipping=5, discount=0.1)
# In general use positional arguments but if you are using integers for better undrstanding use keyword arguments
