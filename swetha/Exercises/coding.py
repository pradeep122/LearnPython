# Write a function that returns the maximum of two numbers.


def maximum(x, y):
    if x > y:
        return x
    if x < y:
        return y


print(maximum(-1, -2))


# Write a function called fizz_buzz that takes a number.

#     If the number is divisible by 3, it should return “Fizz”.
#     If it is divisible by 5, it should return “Buzz”.
#     If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#     Otherwise, it should return the same number.


def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


print(fizz_buzz(9))


# Write a function for checking the speed of drivers.
# This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70),
# it should give the driver one demerit point and
# print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points,
# the function should print: “License suspended”

# def speed_of_drivers(speed):
#     points = 0
#     extra_speed = 5
#     if speed < 70:
#         print("Ok")
#     elif:


#     if points > 12:
#         print("Licence suspended")


# Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit
# with a label to identify the even and odd numbers.
# For example, if the limit is 3, it should print:

#     0 EVEN
#     1 ODD
#     2 EVEN
#     3 ODD

def showNumbers(limit):
    for number in range(0, limit):
        if number % 2 == 0:
            print(f"{number} {'EVEN'}")
        else:
            print(f"{number} {'ODD'}")


print(showNumbers(5))


# Write a function that returns the sum of multiples
# of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return
# the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def sum_of_multiples(limit):
    for number in range(0, limit):
        if (number % 3 == 0) or (number % 5 == 0):
            print(number)


print(sum_of_multiples(20))


# Write a function called show_stars(rows).
# If rows is 5, it should print the following:

#     *
#     **
#     ***
#     ****
#     *****

def show_stars(rows):
    for number in range(rows):
        print("*" * number)


print(show_stars(5))


# Write a function that prints all the prime numbers
#  between 0 and limit where limit is a parameter.
# def is_prime(input):


# def prime_numbers(limit):
#     for number in range(0, limit):
#         is_prime(number)
#         print(number)


# print(prime_numbers(20))
