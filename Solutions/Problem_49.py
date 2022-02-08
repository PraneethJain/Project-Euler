from prime import primelist
from itertools import permutations
from time import time


t1=time()
temp_list=primelist(10000)
prime_list=[i for i in temp_list if i>1487]
for prime in prime_list:
    permutated_strlist=list(permutations(str(prime)))
    L=set([int(''.join(ele)) for ele in permutated_strlist if int(''.join(ele))>1000])
    L=list(L.intersection(prime_list))
    L.sort()
    if len(L) >=3:
        for i in range(len(L)):
            for j in range(i+1,len(L)):
                if 2*(L[j])-L[i] in L:
                    print(L[i],L[j],2*L[j]-L[i])
                    print(f'Process completed in {time()-t1}s')
                    raise SystemExit
