# Write a function for checking the speed of drivers. This function should have one parameter: speed.
#    - If speed is less than 70, it should print “Ok”.
#    - Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#    - If the driver gets more than 12 points, the function should print: “License suspended”


def speed_limit(speed):
    demerit_points = 0
    if speed < 70:
        return "Ok"
    demerit_points = (speed - 70) // 5
    if demerit_points < 12:
        return f"Points: {demerit_points}"
    else:
        return "License suspended"


print("Speed Limit 70 - ", speed_limit(70))
print("Speed Limit 100 - ", speed_limit(100))
print("Speed Limit 60 - ", speed_limit(60))
print("Speed Limit 180 - ", speed_limit(180))
