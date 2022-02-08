from prime import primelist, primecheck
from time import time
t1=time()
i=9
while True:
    if primecheck(i)==False:
        square_of_list=[]
        prime_list=primelist(i)
        for prime in prime_list:
            square_of_list.append(((i-prime)/2)**0.5)
        if any(int(j)==j for j in square_of_list):
            pass
        else:
            print(i,time()-t1)
            break
    i += 2
