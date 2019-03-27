import math
x = 1
x = 1.1
x = 1 + 2j    # a+ bi
print(10 + 3)  # addition operator
print(10 - 3)  # subtraction operator
print(10 * 3)  # multiplication operator
print(10 / 3)  # division operator returns the quotient with floating number
print(10 // 3)  # division operator returns the quotient with integer number
print(10 % 3)  # modulus operator returns remainder
print(10 ** 3)  # exponent operator returns 10 to the "power of" 3


x = 10
# x = x + 3
x += 3  # augument assignment operator

print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))
print(math.floor(2.2))

x = input("x: ")
# print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")


# int(x)
# float(x)
# bool(x)
# str(x)


# Falsy value
# ""
# 0
# none

print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True
print(bool(5))  # True
print(bool(""))  # False
print(bool("False"))  # True
print(bool(False))  # False
