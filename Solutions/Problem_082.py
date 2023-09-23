from rich import print
from time import time

t1 = time()
with open(r"files\p082_matrix.txt") as f:
    matrix = f.readlines()
matrix = [ele.strip() for ele in matrix]
for i, ele in enumerate(matrix):
    matrix[i] = list(map(int, ele.split(",")))

ans = []
for i in range(80):
    ans.append(matrix[i][79])

# Getting min columns from right to left
for column in range(78, -1, -1):
    ans[0] += matrix[0][column]

    # Getting min by going down
    for row in range(1, 80):
        ans[row] = min(
            ans[row - 1] + matrix[row][column], ans[row] + matrix[row][column]
        )
    # Getting min by going up
    for row in range(78, -1, -1):
        ans[row] = min(ans[row + 1] + matrix[row][column], ans[row])

print(min(ans))
print(f"Process completed in {time()-t1}s")
