numbers = [3, 7, 5, 4, 8]
# creates a copy of numbers and any changes made in numbers will not get changed in numbers2
numbers2 = numbers.copy()
numbers.append(13)  # will add 13 to the list
print(numbers)
numbers.insert(1, 10)   # will insert the number in the list where we wanted
print(numbers)
numbers.remove(4)   # will remove the number from list
print(numbers)
# numbers.clear()  # will clear the list
# print(numbers)
print(numbers.index(5))  # will result the last number in the list
# will get the number of occurences of the number in the list
print(numbers.count(5))
numbers.sort()   # sorts the list default in ascending order
print(numbers)
numbers.reverse()  # sorts the list in descending
print(numbers)
print(numbers2)
