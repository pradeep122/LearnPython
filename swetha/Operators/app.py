high_income = False
good_credit = True
student = False
# AND Operator

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# OR Operator

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# NOT Operator
if not student:
    print("Eligible")
else:
    print("Not Eligible")

# Combining All Operators

if (high_income or good_credit) and not student:
    print("ELigible")
else:
    print("Not Eligible")

# Short Circuiting(If the first operand is true so it won't check for the
# other operands to true)
high_income = True
good_credit = True
student = True

if not student and high_income and good_credit:
    print("eligible")

# age should be between 18 and 65
age = 22
# Chaining comparison operator
if 18 <= age < 65:
    print("Eligible")
