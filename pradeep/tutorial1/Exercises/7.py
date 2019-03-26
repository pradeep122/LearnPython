# Write a function that prints all the prime numbers between 0
# and limit where limit is a parameter.


def print_primes(limit):
    for number in range(0, limit + 1):
        if is_prime(number):
            print(number)


def is_prime(prime):
    for number in range(2, prime // 2 + 1):
        if prime % number == 0:
            return False
    return True


print(f" Primes until 0")
print_primes(0)


print(f" Primes until 1")
print_primes(1)


print(f" Primes until 5")
print_primes(5)


print(f" Primes until 23")
print_primes(23)


# print(f" Primes until 400")
# print_primes(400)
