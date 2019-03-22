# Write a function for checking the speed of drivers. This function should
# have one parameter: speed.
#
#   1. If speed is less than 70, it should print “Ok”.
#   2. Otherwise, for every 5km above the speed limit (70), it should give
# the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
#   3. If the driver gets more than 12 points, the function should
# print: “License suspended”


def check_speed(speed):
    if speed < 0:
        return "Speed cant ne negative"
    if speed < 70:
        return "OK"
    points = (speed - 70) // 5
    if points > 12:
        return "License suspended"
    return f"Points: {points}"


print(f"""
-- Check Driver Speed

check_speed(-10)  - {check_speed(-10)}
check_speed(0)    - {check_speed(0)}
check_speed(69)    - {check_speed(69)}
check_speed(70)    - {check_speed(70)}
check_speed(74)    - {check_speed(74)}
check_speed(75)    - {check_speed(75)}
check_speed(76)    - {check_speed(76)}
check_speed(80)    - {check_speed(80)}
check_speed(86)    - {check_speed(86)}
check_speed(130)    - {check_speed(130)}
check_speed(134)    - {check_speed(134)}
check_speed(135)    - {check_speed(135)}
check_speed(150)    - {check_speed(150)}
check_speed(12345667890)    - {check_speed(12345667890)}
""")
