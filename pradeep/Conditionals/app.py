# If Else Conditional Statements

temperature = 15
if temperature > 30:
    print("It's Warm")
    print("Drink Water")
elif temperature > 20:
    print("It's Pleasant")
else:
    print("It's cold")
print("Done")


# Ternary Operator
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# Logical Operators
# and or not

high_income = True
good_credit = True
student = False

if high_income or good_credit or not student:
    print("Eligible")


# Chaining operators
# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")
