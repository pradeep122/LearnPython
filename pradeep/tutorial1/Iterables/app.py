
# range is a complex type in Python
print(type(5))
print(type(range(5)))

# range returns an Iterable which can be used in for loops
# String is also an Iterable
# list is also an iterable

print("------ Range Iterables")
for number in range(5):
    print(number)


print("------ String Iterables")
for letter in "Python":
    print(letter)

print("------ List Iterables")
for number in [1, 2, 3, 5]:
    print(number)
