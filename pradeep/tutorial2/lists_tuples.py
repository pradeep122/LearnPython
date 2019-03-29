# Lists and Maps

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])
print(names[2:4])
print(names[:])

names[0] = 'Pradeep'
print(names[0])


# 2-Dimensional Lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][1])

matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)


# List operations
print(' --- List operations')
numbers = [5, 2, 1, 7, 4]
print(numbers)

print(' --- insert at index')
numbers.insert(0, 10)
print(numbers)

print(' --- remove from list')
numbers.remove(5)
print(numbers)

print(' --- pop from list')
print(numbers.pop())
print(numbers)


print(' --- check if an item exists in a list')
print(numbers.index(2))
# print(numbers.index(50))  # Throws an exception
print(50 in numbers)  # does not throw an exception


print(' --- sort list in place')
numbers.sort()
print(numbers)


print(' --- reverse list in place')
numbers.reverse()
print(numbers)

print(' --- Copy List')
numbers2 = numbers.copy()
numbers.append(20)

print(numbers)
print(numbers2)


print(' --- Clear all items from list')
numbers.clear()
print(numbers)


# Tuples

numbers = (1, 2, 3)
# numbers[0] = 10     # Tuples are immutable, cannot be changed
print(numbers[0])

# Unpacking

coordinates = (1, 2, 3)
product = coordinates[0] * coordinates[1] * coordinates[2]
print(product)

x, y, z = coordinates
product = x * y * z
print(f'x - {x}, y - {y}, z - {z}')

# Dictionries

customer = {
    'name': 'Pradeep Varma',
    'age': 33,
    # 'age': 40,  ## Does not accept duplicate keys
    'is_verified': True
}

print(customer['name'])
# print(customer['Name'])  # Throws an error
print(customer.get('name'))  # Returns None if key does not exist

#  Key value pairs can be added dynamically
customer['birthdate'] = 'Dec 17 1985'
print(customer)
