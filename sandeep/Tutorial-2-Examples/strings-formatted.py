# Formatted strings are useful in situation where we want to dynamically generate some text with variables
first_name = 'Sandeep'
last_name = 'Varma'
# message = first_name + ' [' + last_name + '] is a coder' - hard to visualize the output
message = f'{first_name} [{last_name}] is a coder'
print(message)

#  Formatted strings - prefix your with an f and use {} to dynamically insert value in to your strings
