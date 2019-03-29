
number_map = {
    '1': ' One',
    '2': ' Two',
    '3': ' Three',
    '4': ' Four',
    '5': ' Five',
    '6': ' Six',
    '7': ' Seven',
    '8': ' Eight',
    '9': ' Nine',
    '0': ' Zero'
}


number = input("Phone: ")
string_number = ""
for digit in number:
    digit_string = number_map.get(digit)
    if digit_string is None:
        print("Invalid Phone number, only numbers allowed.")
        break
    else:
        string_number += digit_string

print(string_number)
