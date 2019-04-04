import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 30))

members = ["Pradeep", "Sandeep", "Swetha"]
leader = random.choice(members)
print(leader)
