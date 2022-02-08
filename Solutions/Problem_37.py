from prime import primelist,primecheck
from time import time

t1=time()
prime_list=set(primelist(10**6))
ans=[]
for prime in prime_list:
    if prime>10:
        part_prime1=''
        part_prime2=''
        L=set()
        for letter in str(prime):
            part_prime1+=letter
            L.add(int(part_prime1))
        for letter in str(prime)[::-1]:
            part_prime2+=letter
            L.add(int(part_prime2[::-1]))
        if all(primecheck(i) for i in L):
            ans.append(prime)
    if len(ans)==11:
        break
print(sum(ans))
print(f'Process completed in {time()-t1}s')