from prime import primecheck
from itertools import permutations
from time import time


t1 = time()
all_list=[]

for j in range(8):
    if j==0:
        num_str='123456789'
    else:
        num_str='123456789'[:-j]
    L=list(permutations(num_str))
    num_list=[]
    for element in L:
        num_list.append(''.join(element))
    num_list=list(map(int,num_list))
    all_list.extend(num_list)

all_list.sort(reverse=True)

for num in all_list:
    if primecheck(num):
        print(num)
        break
print(f'Process completed in {time()-t1}s')