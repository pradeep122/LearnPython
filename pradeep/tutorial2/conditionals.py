

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


has_high_income = True
has_good_credit = False
has_criminal_record = False

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")


temparature = 30

if temparature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")


name = input('Enter your Name: ')

name_length = len(name)
if name_length < 3:
    print("Name must be atleast 3 characters long")
elif name_length > 30:
    print("Name cannot exceed 50 characters")
else:
    print(f"Name [{name}] looks good!")
