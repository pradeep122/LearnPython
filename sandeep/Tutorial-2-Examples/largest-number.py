# Write a program to find the largest number in the list

numbers = [3, 6, 1, 8, 2]
maximum = numbers[0]
for max in numbers:
    if max > maximum:
        maximum = max
print(maximum)
