# How to pass info to functions
# Parameters are placeholders for recieveing information
#  Arguments are actual pieces of info we supply to functions


def greet_user(name):
    print(f'Hi {name}')
    print('Welcome Aboard')


greet_user("Sandeep")
greet_user("Pradeep")

# Multiple parametrs examplr


def greet_users(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome Aboard')


greet_users("Sandeep", "D")
greet_users("Pradeep", "D")
