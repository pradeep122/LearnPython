# We use Dictionaries where we want to store
# the information that comes as key - value pairs


# Empty Dictionary
empty = {}

# Dictionary with key - value pairs
# Each key in the dictionary should be unique
# Values can be String, integer, float, boolean, list, tuple
customer = {
    "name": "Vijayalakshmi",
    "age": 27,
    "is_verified": True
}

# Accessing values from the dictionary
# using [] brackets passing key to it
print(customer["name"])

# If key is not there in dictionary
# print(customer["phone"])  # KeyError: 'phone'

# Keys are case sensitive
# we can not pass "Name" instead of "name"
# print(customer["Name"])  # KeyError: 'Name'

# Instead of [] brackets to access the value
# we can use get() method
print(customer.get("age"))

# if key is not there it won't generate an error
# instead it returns "none" represents absence of value
print(customer.get("date"))


# We can also supply default value
# if key is not there in dictionary
print(customer.get("date", "Swetha"))


# We can update the value of a key
customer["name"] = "Vijayalakshmi Kalidindi"
print(customer)

# We can also add a new key
customer["DOB"] = "6 March 1992"
print(customer)
