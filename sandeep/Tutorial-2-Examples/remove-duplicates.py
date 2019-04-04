# Remove duplicates in a list

numbers = [3, 5, 8, 3, 5, 4, 9]
for duplicate in numbers:
    x = numbers.count(duplicate)
    if x > 1:
        numbers.remove(duplicate)
print(numbers)
