birth_year = input('Birth year: ')
# age = 2019 - birth_year - using this line we will get error as the birth year would be a string
# int() - converts a string to integer
# float() - to float
# bool() - to boolean value
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)
