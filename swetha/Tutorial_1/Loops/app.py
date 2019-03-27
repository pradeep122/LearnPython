# For loop

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):  # 2 steps forward
    print("Attempt", number, number * ".")

# Break and For Else Loop

# if loop is successful then it breaks and
# won't perform the else block otherwise if block is
# failed then else block will be executed


successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

print("*************** Nested Loops *********")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


print("**************** while Loop *********")
number = 100
while number > 0:
    print(number)
    number //= 2


command = ""
while (command.lower() != "quit"):
    command = input(">")
    print("ECHO", command)


print("************* Infinite Loop ***********")

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
