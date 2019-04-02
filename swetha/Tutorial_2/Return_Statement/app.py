# If we didn't specify return statement in a function
# By default all functions return none


def square(number):
    return number * number
    # print(number * number)


print(square(3))  # 9
print(square(4))  # 16 and none if we didn't return
