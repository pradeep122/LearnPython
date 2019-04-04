# A module in python is basically a file with some code
# We use modules to organise our code into files

# We can directly import by using the file name and
# we need to call the methods using the object

# import converters
# print(converters.kg_to_lbs(1000))

# We can import the method from converters directly
from converters import kg_to_lbs
print(kg_to_lbs(1000))
