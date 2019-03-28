# While Loops
#number = 100
# while number > 0:
#   print(number)
#  number //= 2

# Example

command = ""
# while command != "quit" and command != "QUIT": # Program does not terminate if we enter "Quit"
# Program will convert the input string to lower and compare to quit to terminate
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
