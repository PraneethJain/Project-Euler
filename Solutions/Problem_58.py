from prime import primecheck
from time import time

# side length: (2n+1)
# center to top right: (2n+1)^2
# center to top left: (2n+1)^2-2n
# center to bottom left:(2n+1)^2-4n
# center to bottom right:(2n+1)^2-6n
# number of diagonal numbers: (4n+1)


t1=time()
diag_nums=set()
prime_nums=set()
n=1
ans=1
while ans>0.1:
    a2=(2*n+1)**2-2*n
    a3=(2*n+1)**2-4*n
    a4=(2*n+1)**2-6*n
    if primecheck(a2):
            prime_nums.add(a2)
    if primecheck(a3):
            prime_nums.add(a3)
    if primecheck(a4):
            prime_nums.add(a4)
    ans=len(prime_nums)/(4*n+1)
    n+=1
print(2*n-1)
print(f'Process completed in {time()-t1}s')