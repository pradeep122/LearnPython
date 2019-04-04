names = ['Nirvaan', 'Swetha', 'Pradeep', 'Sowmya']
print(names)
print(names[0])
print(names[-1])
print(names[2])
# it returns all the items starting from index 1
print(names[1:])  # ['Swetha', 'Pradeep', 'Sowmya']
# it returns the items starting
# from index 1 but not including index 3
print(names[1:3])  # ['Swetha', 'Pradeep']
# it returns all the items starting from index 0 to index 3
# by default it takes the value 0 to last index
print(names[:])  # ['Nirvaan', 'Swetha', 'Pradeep', 'Sowmya']
