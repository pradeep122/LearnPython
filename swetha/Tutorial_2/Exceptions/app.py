# Exceptions are used to handle the errors in the python program
# In a program exit code = 1, means program "Crashed"
# code = 0 means "Success"

# An exception is a kind of error that crashes our program
# We use try, except block to handle exceptions that are raised in the programs

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)

except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")

# age = 26
# age = 0 (Age cannot be zero)
# age = swetha (Invalid value)
