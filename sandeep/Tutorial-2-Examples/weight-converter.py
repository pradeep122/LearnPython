# Write a program to take weight as input either kg or lbs and convert into other.

your_weight = input("Please enter your weight: ")
mass = input("(L)bs or (K)g: ")
if mass.upper() == "K":
    converted_weight = int(your_weight) * 2.2
    print(f"You are {int(converted_weight)} pounds")
elif mass.upper() == "L":
    converted_weight = int(your_weight) * 0.45
    print(f"You are {int(converted_weight)} kilos")
else:
    print("Invalid input")
