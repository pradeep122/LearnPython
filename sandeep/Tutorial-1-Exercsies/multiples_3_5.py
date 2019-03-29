# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


def sum_multiples(limit):
    total = 0
    for numbers in range(1, limit):
        if (numbers % 3 == 0) or (numbers % 5 == 0):
            total += numbers
    print(f"{'Total = '} {total}")


sum_multiples(11)
