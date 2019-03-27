# Comparison Operator is used in a situation
# where we want to compare the variable with a value
# EXERCISE
# if name is less than 3 characters long
#   name must be atleast 3 characters
# otherwise if its more than 50 characters long
#   name can be a maximum of 50 characters
# otherwise
#   name looks good!

# MY SOLUTION
name = "dia"
if len(name) < 3:
    print("name must be atleast 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")

# TEST CASES
# name = swetha (name looks good!)
# name = Li (name must be atleast 3 characters)
# name = jdfjdjfjdjfjdjfjkdjfjfjdjfjdjkjfdsfjksdfjdhfjdhjfkdhjdshfjdhfdfdj
# (name can be a maximum of 50 characters )
# name = dia (name looks good!)
