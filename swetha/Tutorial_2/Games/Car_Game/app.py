# MY SOLUTION
command = " "
is_running = False

while command != 'quit':
    command = input(">")
    if command == 'help':
        print("""
            start - to start the car
            stop - to stop the car
            quit - to exit
        """)
    elif command.lower() == 'start':
        if not is_running:
            print("Car started...Ready to go!")
        else:
            print("Car already started...")
        is_running = True
    elif command.lower() == 'stop':
        if is_running:
            print("Car stopped..")
        else:
            print("Car already stopped...")
        is_running = False

    elif command.lower() == 'quit':
        break
    else:
        print("I don't understand that...")

# ACTUAL SOLUTION
command = " "
started = False

while command != 'quit':
    command = input(">")
    if command == 'help':
        print("""
            start - to start the car
            stop - to stop the car
            quit - to exit
        """)
    elif command.lower() == 'start':
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started")

    elif command.lower() == 'stop':
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped")

    elif command.lower() == 'quit':
        break
    else:
        print("I don't understand that...")


# SOLUTION 2
# while(True):
#     command = input(">")
#     if command.lower() == 'help':
#         print("""
#             start - to start the car
#             stop - to stop the car
#             quit - to exit
#         """)
#     elif command.lower() == 'start':
#         print("Car started...Ready to go! ")
#     elif command.lower() == 'stop':
#         print("Car stopped")
#     elif command.lower() == 'quit':
#         break
#     else:
#         print("I don't understand that...")
