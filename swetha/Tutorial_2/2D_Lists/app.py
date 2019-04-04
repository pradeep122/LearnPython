# Two - Dimensional list is a list where each item in that list is another list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

# to get the first item from the matrix
print(matrix[0][0])  # 1

# to get second row second element
print(matrix[1][1])  # 5

# We can also assign a new value to it
matrix[2][1] = 23
print(matrix)  # [[1,2,3], [4,5,6], [7,23,9]]

# We can also use nested loops to it
for row in matrix:
    for item in row:
        print(item)
