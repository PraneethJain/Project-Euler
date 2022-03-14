from itertools import product
from time import time


def check(c1, c2):
    return sorted(list(str(c1))) == sorted(list(str(c2)))


t1 = time()
cube_list = [i**3 for i in range(10**3, 10**4)]
for c1, c2 in product(cube_list, repeat=2):
    if c2 > c1 and check(c1, c2):
        for c3 in cube_list:
            if c3 > c2 and check(c2, c3):
                for c4 in cube_list:
                    if c4 > c3 and check(c3, c4):
                        for c5 in cube_list:
                            if c5 > c4 and check(c4, c5):
                                print(c1, c2, c3, c4, c5)
                                print(f"Process completed in {time()-t1}s")
                                raise SystemExit
