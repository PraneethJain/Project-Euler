from rich import print
from time import time
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

t1 = time()
with open(r"files\p083_matrix.txt") as f:
    matrix = f.readlines()
matrix = [ele.strip() for ele in matrix]
for i, ele in enumerate(matrix):
    matrix[i] = list(map(int, ele.split(",")))

grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(79, 79)
finder = AStarFinder()
path, _ = finder.find_path(start, end, grid)

sum = 0
for column, row in path:
    sum += matrix[row][column]

print(sum)
print(f"Process completed in time {time()-t1}s")
