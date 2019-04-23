import random

for i in range(3):
    print(random.randint(10, 20))

members = ['Sandeep', 'Pradeep', 'Swetha', 'Sravya']
leader = random.choice(members)
print(leader)
