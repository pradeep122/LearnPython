# String Methods

course = "   Python Programming"
print(course.upper())  # Changes to upper case
print(course.lower())  # Changes to lower case
print(course.title())
# Strips empty spaces "lstrip" and "rstirp" for stripping left and right spaces
print(course.strip())
print(course.find("Pro"))  # Returns the index Value
# Replaces the word "p" with "j" in the entire string
print(course.replace("P", "j"))
print("Pro" in course)  # Returns boolean values True or False
print("swift" not in course)  # Returns boolean values
