#  Write a function that returns the maximum of two numbers.


def max(number1, number2):
    return number1 if (number1 >= number2) else number2


print(f"""
-- function that returns the maximum of two numbers.

max(0,0)    - {max(0,0)}
max(10,10)  - {max(10,10)}
max(5,9)    - {max(5,9)}
max(9,6)    - {max(9,6)}
max(-1,-6)  - {max(-1,-6)}
""")
