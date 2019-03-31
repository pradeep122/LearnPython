# List methods are the methods or functions we use them to the lists


# append() - it adds the number at the end of the list
numbers = [5, 2, 1, 7, 4, 1]
numbers.append(10)
print(numbers)

# insert() - it adds the number in between the list or
# beginning of the list.
# It takes two values:
# 1. index value
# 2. object value

numbers.insert(0, 16)
numbers.insert(4, 33)
print(numbers)


# remove() - we can remove an item from the list
numbers.remove(16)
print(numbers)

# clear() - it removes the entire list
# we don't need to pass any value to it we simply call clear()

# numbers.clear()
# print(numbers) # [] empty list

# pop() - it removes the item from end of the list
numbers.pop()
print(numbers)

# index() - To check for the existence of an item in the list.
# It returns the index value
print(numbers.index(7))  # 4
# print(numbers.index(50))  # we get ValueError because its not in list

# in - Its also used to check the exixtence of an item in the list.
# It returns the boolean value
# print(50 in numbers)  # False
print(5 in numbers)  # True

# count() - for counting the occurences of an item in a list
print(numbers.count(1))  # 2

# sort() - to sort the items in the list.
# sort() doesn't take any value.
# Its an object in python represents absence of a value.
print(numbers.sort())  # None (it doesn't returns any value it simply sorts)
# Instead of printing we simply call
numbers.sort()
print(numbers)  # [1,1,2,4,5,7,33]

# reverse() - it sorts in decending order
numbers.reverse()
print(numbers)  # [33,7,5,4,2,1,1]

# copy() - we can get a copy of the list.
# numbers2 is the copy of original list.
numbers2 = numbers.copy()
# Adding new operations to the original list will not effect the second list
numbers.append(23)
print(numbers2)
print(numbers)
