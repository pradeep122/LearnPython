students_count = 1000
rating = 4.99
is_published = False

# This is a comment
# Escape sequences
# \"
# \'
# \\
# \n

course_name = "Python\n\t \"\\\'Programming"
print(len(course_name))
print(course_name)


first = "Pradeep"
last = "Dantuluri"
full = first + " " + last
formatted_full = f"{first} {last} {len(full)} jkhkjlasdfjhkhsd dfsabsksadf"
normal_full = first + " " + last + " " + str(len(full))
print(full)
print(formatted_full)
print(normal_full)
