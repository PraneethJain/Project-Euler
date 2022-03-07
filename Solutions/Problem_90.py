# 01,04,09,16,25,36,49,64,81
from rich import print
from time import time
from itertools import combinations


def check(dice1, dice2):
    squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]
    for i in range(9):
        if not (
            ((squares[i][0] in dice1) and squares[i][1] in dice2)
            or ((squares[i][0] in dice2) and squares[i][1] in dice1)
        ):
            return False
    return True


t1 = time()
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
combs = combinations(digits, 6)
combs = [set(comb) for comb in combs]
for comb in combs:
    if 9 in comb:
        comb.add(6)
    if 6 in comb:
        comb.add(9)

ans = 0
for dice1 in combs:
    for dice2 in combs:
        if check(dice1, dice2):
            ans += 1

print(ans // 2)  # dice1 and dice2 are not distinct
print(f"Process completed in {time()-t1} seconds")
