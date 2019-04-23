# Dictionaries in Python
# Name: Sandeep
# Email: varma.576@gmail.com
# Phone : 9000252599
# With {} we can define a dictionary
# Each key should be unique in the dictionary.
customer = {
    "name": "Sandeep",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
# print(customer["Name"]) we will get error as the key does not exist
# We will get "None insted of error if we use .get"
print(customer.get("birthdate"))
# will return the default value we declared
print(customer.get("phone", 9000252599))
customer["birthdate"] = "Jun 12 1987"
print(customer["birthdate"])
