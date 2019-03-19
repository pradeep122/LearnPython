
# For Loops
print("-------------- For Loops -----------------")
for number in range(1, 10, 2):
    print("Attempt", number, "." * (number))


# For Else Loops

print("-------------- For Else Loops ------------")
successful = False
for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# Nested Loops
print("-------------- Nested Loops --------------")
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print("-------------- While Loops --------------")
number = 100
while number > 0:
    print(number)
    number //= 2

print("-------------- While Loops with input --------------")

command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)


print("-------------- Infinite Loops -------------")

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
