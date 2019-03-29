# Write a function called show_stars(rows).
# If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****


def show_stars(rows):
    for stars in range(1, rows + 1):
        print((stars) * "*")
#   for stars in range(0, rows):
#       print((stars +1) * "*")


print("If rows are 3\n")
show_stars(3)
print("\nIf rows are 5\n")
show_stars(5)
print("\nIf rows are 1\n")
show_stars(1)
