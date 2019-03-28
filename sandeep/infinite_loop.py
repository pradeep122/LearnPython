# Infinite Loop
# We do not have define command variable as we do not have infinite loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
