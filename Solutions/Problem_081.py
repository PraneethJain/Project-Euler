from time import time
from rich import print

t1 = time()
with open(r"files\p081_matrix.txt") as f:
    matrix = f.readlines()
matrix = [ele.strip() for ele in matrix]
for i, ele in enumerate(matrix):
    matrix[i] = list(map(int, ele.split(",")))

for i in range(78, -1, -1):
    matrix[79][i] += matrix[79][i + 1]
    matrix[i][79] += matrix[i + 1][79]

for i in range(78, -1, -1):
    for j in range(78, -1, -1):
        matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

print(matrix[0][0])
print(f"Process completed in {time()-t1}s")
