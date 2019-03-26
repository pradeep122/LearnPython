# Write a function called show_stars(rows).
# If rows is 5, it should print the following:
#     *
#     **
#     ***
#     ****
#     *****


def show_stars(rows):
    for row in range(1, rows + 1):
        row_string = ""
        for col in range(1, row + 1):
            row_string += "*"
        print(row_string)


print(" --- 0 rows")
show_stars(0)
print(" --- -1 rows")
show_stars(-1)
print(" --- 1 rows")
show_stars(1)
print(" --- 5 rows")
show_stars(5)
print(" --- 15 rows")
show_stars(15)
