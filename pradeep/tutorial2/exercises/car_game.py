
# Excercise Car Game

car_running = False
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
        if car_running:
            print(" Car is already running!")
        else:
            print("Car Started.. Ready to go!")
        car_running = True
    elif command.lower() == 'stop':
        if not car_running:
            print('Car is already stopped.')
        else:
            print("Car Stopped.")
        car_running = False
    elif command.lower() == 'quit':
        break
    else:
        print("I don't understand that... type 'help' for help")
