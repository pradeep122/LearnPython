students_count = 1000
rating = 4.99
is_published = False
# Escape Sequences
# \"
# \'
# \\
# \n (new line)
# \t (tab)
course_name = "Python \"Programming"
print(course_name)
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])
print(students_count)
print(is_published)

first = "Vijayalakshmi"
last = "Kalidindi"
full = first + " " + last
formatted_full = f"{first} {last} {len(full)}"
print(full)
print(formatted_full)


# Python interprets the code line by line
price = 10  # (initial value)
price = 20  # (reset Value)
print(price)

# exercise for variables
full_name = "John Smith"
age = 18
is_new_patient = True
name = input("What is your name? ")
color = input("what is your favourite color? ")
print(name + " likes " + color)
