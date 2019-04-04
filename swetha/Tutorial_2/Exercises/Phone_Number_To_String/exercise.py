numbers = {
    0: 'zero ',
    1: 'one ',
    2: 'two ',
    3: 'three ',
    4: 'four ',
    5: 'five ',
    6: 'six ',
    7: 'seven ',
    8: 'eight ',
    9: 'nine '
}

phone_number = input("Phone: ")
str = ""
for number in phone_number:
    str = str + numbers[int(number)]
    # str += numbers.get(int(number), "!")
print(str)
