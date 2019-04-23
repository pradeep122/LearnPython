# Write a program to ask for phone number in digits and returns it in words
phone = input("Phone: ")
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}
print(numbers["1"])
result = ""
for ch in phone:
    result += numbers.get(ch) + "-"
print(result)
