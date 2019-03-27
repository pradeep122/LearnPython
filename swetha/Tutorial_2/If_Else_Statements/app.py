
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# is_hot = True
# is_cold = False
# prints
# It's a hot day
# Drink plenty of water
# Enjoy your day

# is_hot = False
# is_cold = True
# prints
# It's a cold day
# Wear warm clothes
# Enjoy your day


# is_hot = False
# is_cold = False
# prints
# It's a lovely day
# Enjoy your day

# EXERCISE

# My solution:
# price = 1000000
# good_credit = False
# bad_credit = False
# down_payment = 0

# if good_credit:
#     down_payment = price * (10 / 100)
#     print(down_payment)
# elif bad_credit:
#     down_payment = price * (20 / 100)
#     print(down_payment)
# else:
#     print(down_payment)


# Solution
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payemnt: ${down_payment}")  # $100000.0
