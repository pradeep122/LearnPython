course = 'Python for Begineers'
# The index of the first character is 0. So it return 2 letter in the string
print(course[1])
print(course[0])  # It returns the first character
print(course[-1])  # -1 returns the last character from the end
print(course[-3])  # -3 returns the last 3rd character from the end
# returns characters starting from 0,1 & 2. # is not included.
print(course[0:3])
# returns charcters from 1 to last if the end index is not supllied
print(course[1:])
# returns character from 0 to 4 when start index is not given
print(course[:5])
