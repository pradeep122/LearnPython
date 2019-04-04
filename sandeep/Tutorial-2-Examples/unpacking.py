# Unpacking

coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x * y * z)
# In python unpacking we can assign x,y,z in the same method as below

a, b, c = coordinates  # Line 4,5,6 & 10 are same
print(a * b * c)

# unpacking is not only limited to tuples it can be used in lists as well
