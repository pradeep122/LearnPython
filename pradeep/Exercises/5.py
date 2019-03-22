# Write a function that returns the sum of multiples of 3 and 5
# between 0 and limit (parameter). For example, if limit is 20,
# it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


def sum_of_multiples(limit):
    sum = 0
    sum_str = ""
    for number in range(limit + 1):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
            sum_str += f"{number}, "
    print(f"Sum of {sum_str} = {sum}")


sum_of_multiples(0)
sum_of_multiples(-1)
sum_of_multiples(20)
