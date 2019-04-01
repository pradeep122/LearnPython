# Unpacking a tuple or lists into variables

# Using Tuple
# coordinates = (1, 2, 3)

# Using List
coordinates = [1, 2, 3]

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x)
print(y)
print(z)

# We can re write the above result using unpacking

# Here, we are assigning the first item from the tuple to variable x
# second item from the tuple is assigned to variable y
# third item from the tuple is assigned to variable z
x, y, z = coordinates
print(x)
print(y)
print(z)
