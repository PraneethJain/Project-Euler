from time import time


t1 = time()
with open(r"files\p067_triangle.txt") as f:
    file = f.read().splitlines()
L = []
for ele in file:
    L.append(list(map(int, ele.split(" "))))

for i in range(len(L) - 2, -1, -1):
    for j in range(0, i + 1):
        if L[i + 1][j] > L[i + 1][j + 1]:
            L[i][j] += L[i + 1][j]
        else:
            L[i][j] += L[i + 1][j + 1]
print(L[0][0])
print(f"Process completed in {time()-t1}s")
