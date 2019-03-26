

# If conditional statements

is_hot = False
is_cold = True

if is_hot:
    print('Its a hot day')
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print('Enjoy your day')


has_good_credit = True
price = 1000000
if has_good_credit:
    print(f"Down Payment: {price * 0.1}")
else:
    print(f"Down Payment: {price * 0.2}")
