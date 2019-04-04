import random
# Generating a random number between 0 to 3
for i in range(3):
    print(random.random())

# Generating integer random numbers between 10 to 20
for i in range(3):
    print(random.randint(10, 20))

memebers = ['swetha', 'Aruna', 'Raju', 'sowmya', 'nirvaan', 'pradeep']
leader = random.choice(memebers)
print(leader)
