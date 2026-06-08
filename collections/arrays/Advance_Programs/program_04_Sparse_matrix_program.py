# program_04_Sparse_matrix_program.py

matrix = [
    [0, 0, 3],
    [0, 0, 0],
    [1, 0, 0]
]

count = 0

for row in matrix:
    for value in row:

        if value == 0:
            count += 1

if count > (len(matrix) * len(matrix[0])) / 2:
    print("Sparse Matrix")
else:
    print("Not Sparse Matrix")