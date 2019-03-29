
# Exercise  - Weight Converter

weight_string = input("Weight: ")
weight = int(weight_string)
units = input("(L)bs or (K)g: ")

if units.lower() == 'k':
    new_weight = round(weight / 0.4535924)
    new_units = "Pounds"
elif units.lower() == 'l':
    new_weight = round(weight * 0.4535924)
    new_units = "Kilograms"


print(f"You are {new_weight} {new_units} ")
