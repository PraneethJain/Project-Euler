from rich import print
from time import time
from rich.progress import track
from itertools import product

t1 = time()
with open(r"files\p096_sudoku.txt") as f:
    file = f.readlines()
file = [ele.strip() for ele in file]
num_list = []
for ele in file:
    try:
        int(ele)
        num_list.append(ele)
    except:
        pass

grids = [
    ([list(map(int, list(ele))) for ele in grid])
    for grid in [num_list[i : i + 9] for i in range(0, 50 * 9, 9)]
]
digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def valid(grid, num, pos):
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    for j in range(9):
        if grid[j][pos[1]] == num and pos[0] != i:
            return False
    for i in range(pos[0] // 3 * 3, pos[0] // 3 * 3 + 3):
        for j in range(pos[1] // 3 * 3, pos[1] // 3 * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find
        for value in digits:
            if valid(grid, value, (row, col)):
                grid[row][col] = value
                if solve(grid):
                    return True
                grid[row][col] = 0


def find_empty(grid):
    for i, j in product(range(9), repeat=2):
        if grid[i][j] == 0:
            return (i, j)


ans = 0
for grid in track(grids, "[red bold]Processing[/red bold]"):
    solve(grid)
    ans += int(str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2]))

print(ans)
print(f"Process completed in {time()-t1} seconds")
