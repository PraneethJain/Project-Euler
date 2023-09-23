from time import time


class DSU:
    def __init__(self, N: int) -> None:
        self._parents = list(range(N))
        self._ranks = [1] * N

    def find(self, u: int) -> int:
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def connected(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)

    def union(self, u: int, v: int) -> bool:
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1
        return False


t1 = time()

with open("../files/p107_network.txt") as f:
    matrix = [
        list(map(lambda x: None if "-" in x else int(x), line.split(",")))
        for line in f.readlines()
    ]

N = len(matrix)
L = sorted([(w, i, j) for i, row in enumerate(matrix) for j, w in enumerate(row) if w])

mst_weight = 0
dsu = DSU(N)
for weight, i, j in L:
    if dsu.find(i) != dsu.find(j):
        mst_weight += weight
        dsu.union(i, j)

print(sum(x[0] for x in L) // 2 - mst_weight)
print(f"Process completeed in {time()-t1}s")
