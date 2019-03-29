# Write a function that prints all the prime numbers between 0 and limit
# where limit is a parameter.


def prime_numbers(limit):
    for number in range(1, limit):
        if check_prime(number):
            print(number)


def check_prime(numbers):
    for number in range(2, numbers):
        if numbers % number == 0:
            return False
    return True


print("Prime numbers till 10\n")
prime_numbers(10)
print("\nPrime numbers till 30\n")
prime_numbers(30)
