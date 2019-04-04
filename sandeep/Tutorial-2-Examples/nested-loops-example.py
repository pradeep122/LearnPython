# numbers = [5, 2, 5, 2, 2]
# xxxxxx
# xx
# xxxxxx
# xx
# xx

# print L

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)
