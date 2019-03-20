# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FIZZBUZZ"
#     elif input % 3 == 0:
#         return "FIZZ"
#     elif input % 5 == 0:
#         return "BUZZ"
#     else:
#         return input


# print(fizz_buzz(30))


# for number in range(20):
#     print(fizz_buzz(number))

# SOLUTION

def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        return "FIZZBUZZ"
    if(input % 3 == 0):
        return "FIZZ"
    if(input % 5 == 0):
        return "BUZZ"
    return input


print(fizz_buzz(7))
