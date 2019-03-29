
numbers = [1, 4, 8, 2, 4, 7, 2, 4, 7, 4, 5, 7, 3, 5, 7, 6, 8]

# Solution without sorting

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)


# Solution using sorting - More complicated

# numbers.sort()

# unique_numbers = numbers[:1]
# placeholder = numbers[0]
# for number in numbers[1:]:
#     if number != placeholder:
#         placeholder = number
#         unique_numbers.append(number)

# print(unique_numbers)
