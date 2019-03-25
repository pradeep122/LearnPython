birth_year = input("What is your birth year? ")
print(type(birth_year))
age = 2019 - int(birth_year)  # string converted to integer
print(type(birth_year))
print(type(age))
print(age)


# Exercise for Type Conversions
weight_lbs = input("Enter Your weight in lbs? ")
weight_kgs = float(weight_lbs) * 0.4535
print("Weight in lbs to kgs: ", weight_kgs)
