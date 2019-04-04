# Weight Converter
# Pounds to Kilograms -> 1lb = 0.45359237kg
# m(kg) = m(lb) * 0.45359237

# Kilograms to Pounds -> 1kg = 2.20462262185lb
# m(lb) = m(kg) / 0.45359237

# MY SOLUTION
weight = input("Weight: ")
converter = input("(l)bs or (K)gs: ")
# print(f"You are {weight} {converter} ")

if converter.lower() == 'k':
    weight = float(weight) / 0.45359237
    print(f"You are {weight} pounds")
else:
    weight = float(weight) * 0.45359237
    print(f"You are {weight} kgs")


# SOLUTION
# Here Input function returns string so we have type casted it to integer
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kgs")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
