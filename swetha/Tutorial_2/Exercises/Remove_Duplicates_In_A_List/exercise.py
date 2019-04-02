# Write a program to remove the duplicates in a list
duplicates_list = [6, 6, 10, 30, 6, 17, 20, 23, 17, 6, 17, 33, 56, 77, 3, 99]
# duplicates_list_copy = duplicates_list.copy()
# for number in duplicates_list:
#     if duplicates_list_copy.count(number) > 1:
#         duplicates_list_copy.remove(number)
# print(duplicates_list_copy)


final_list = []
for number in duplicates_list:
    if number not in final_list:
        final_list.append(number)

print(final_list)
