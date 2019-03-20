temparature = 15
if temparature > 30:
    print("It's warm")
    print("Drink Water")
elif temparature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


age = 22
# if age >= 18:
#    print("Eligible")
# else:
#     print("Not Eligible")

message = "Eligible" if age >= 18 else "Not Eligible"  # Ternary Operator
print(message)
