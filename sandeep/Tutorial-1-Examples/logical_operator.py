# In Python there are 3 Logical operators
# and, or, not
# Example for processing loan

high_income = False
good_credit = True
student = False
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")
# or operator
if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")
# not operator
if not student:
    print("Eligible")
else:
    print("Not Eligible")
# Person is eligble if either high income or good credit and not a student
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
