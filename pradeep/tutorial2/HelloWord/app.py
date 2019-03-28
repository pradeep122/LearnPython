
print("Pradeep Varma Dantuluri")
print('o----')
print(' ||||')

print("*" * 10)

price = 10
price = 20  # integer
rating = 4.9  # float
name = 'Mosh'  # string
is_published = False  # boolean
print(price)

name = "John Smith"
age = 20
is_new = True

# Console Input
name = input("What is your name? ")
color = input("What is your favourite color? ")
print(name + ' likes ' + color)

# Type Conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

weights_lbs = input('Weight (lbs): ')
weight_kg = 0.4535924 * float(weights_lbs)
print('Weight (kgs): ' + str(weight_kg))

# Strings
course1 = "Python's course for Beginners"
course2 = 'Python course for "Beginners"'
course3 = '''
Hi Pradeep,

Here is our first email to you,

Thanks and Regards
Pradeep
'''
print(course1)
print(course2)
print(course3)

print(course1[0])  # first character
print(course1[-1])  # last character
print(course1[0:3])  # first 3 characters
print(course1[1:])  # All but the 1st character
print(course1[:-1])  # All but the last character
print(course1[:])  # copy of the entire string

# Formatted Strings
first = 'John'
last = "Smith"
message = f"{first} [{last}] is a coder"
print(message)


# Stirng Methods

course = 'Python for Beginners'
print(len(course))  # general pupose fucntion , can be used for lists as well
# String specific methods
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.find('o'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print('python' in course)


# Operators

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # Integer division
print(10 % 3)  # modulus (remainder)
print(10 ** 3)  # Power
