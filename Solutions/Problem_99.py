from rich import print
from time import time
from math import log10 as log


t1 = time()
with open(r"files/p099_base_exp.txt") as f:
    file = f.readlines()
file = [tuple(map(int, ele.strip().split(","))) for ele in file]
file = list(map(lambda tup: tup[1] * log(tup[0]), file))
print(file.index(max(file)) + 1)
print(f"Process completed in {time()-t1} seconds")
