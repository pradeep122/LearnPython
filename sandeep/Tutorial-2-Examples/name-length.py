# if name is less than 3 characters long
#    name must be at least 3 characters
# otherwise if it's more than 50 characters
#    name can be maximum of 50 characters
# otherwise
#    name lokks good

name = "Sandeep"
# name = "S"
# name = "qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must not be more than 50 characters")
else:
    print("Name looks good")
