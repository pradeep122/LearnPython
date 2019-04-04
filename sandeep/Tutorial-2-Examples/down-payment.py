# Price of a house is $1M
# If buyer has good credit,
# they need to put down 10% otherwiswe 20%
# Print the down payment

if_good_credit = False
price = 10000000
down_payment = 0
if if_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment is {down_payment}")
