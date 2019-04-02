# Write a program to find the largest number in a list?

numbers = [2, 56, 33, 80, 23, 16, 10, 100, 89, 111, 65, 47]
max = numbers[0]
for number in numbers[1:]:
    if max <= number:
        max = number
print(f"Maximum Number: {max}")
