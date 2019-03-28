
# Excercise Car Game

while True:
    command = input('> ')

    if command.lower() == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        help - print this help message
        """)
    elif command.lower() == 'start':
        print("Car Started.. Ready to go!")
    elif command.lower() == 'stop':
        print("Car Stopped.")
    elif command.lower() == 'quit':
        break
    else:
        print("I don't understand that... type 'help' for help")
