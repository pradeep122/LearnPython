# > help
# start - to start the car
# stop - to stop the car
# quit - exit
# > start
#   Car started. Ready to go
# > stop
#    Car stopped
# > quit
# > unknown string
#   I don't understand that
# If the car is already started or stopped it should result the same


manual = ""
started = False
while True:
    manual = input("> ")  # Can be given as manual = input("> ").lower()
    if manual.lower() == "help":
        print('''
start - to start the car
stop - to stop the car
quit - exit
        ''')
    elif manual.lower() == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started. Ready to go")
    elif manual.lower() == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif manual.lower() == "quit":
        break
    else:
        print("I don't understand that.")
