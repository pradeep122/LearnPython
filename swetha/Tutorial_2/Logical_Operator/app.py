# we use this logical operator in a situation where it has multiple conditions
# Logical Operators are of Three types:
# AND(always or both true)
# OR (atleast one condition is true)
# NOT

# if applicant has high income and good credit
# Eligible for Loan

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for Loan")

# if applicant has high income or good credit
# Eligible for Loan

if has_high_income or has_good_credit:
    print("Eligible for Loan")

# If applicant has good credit and doesn't have a criminal record
# Eligible for loan

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
