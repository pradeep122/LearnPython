course = "  Python Programming  "
print(course.upper())
print(course.lower())
print(course.title())
# print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course.find("gram"))
print(course.find("Gram"))
print(course.replace("P", "s"))
print("Pro" in course)
print("swift" not in course)

new_course_name = "Python's course for Beginners"
another_course_name = 'Python for "Beginners"'
print(new_course_name)
print(another_course_name)

message = """
Hi Nirvaan,

This is my first email to you.

Love you..

Regards,
Mumma


"""

print(message)


# Exercise
name = "Jennifer"
print(name[1:-1])  # "ennife"

course_name = "Python for Beginners"
print(len(course_name))  # 20
print(course_name.upper())  # PYTHON FOR BEGINNERS
print(course_name.lower())  # python for beginners
print(course_name.find("p"))  # -1
print(course_name.find("o"))  # 4
# find method gives the index of the first occurence of the character
print(course_name.replace('Beginners', 'Absolute Beginners'))
# Python for Absolute Beginners
print("python" in course_name)  # False
