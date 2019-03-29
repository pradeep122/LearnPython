# In python logical operators are short circuited

high_income = False
good_credit = True
student = True
# The evaluation stops if either of the "and" is false
if high_income and good_credit and not student:
    print("Eligible")
# # The evaluation stops if either of the "and" is false
if high_income or good_credit or not student:
    print("Eligible")
