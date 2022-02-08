from math import *
from prime import primecheck

prime_list=[2]+[i for i in range(1,1000000,2) if primecheck(i)]
truncate=[]
for i in prime_list:
    if i<10:
        pass
    else:
        prime=str(i)
        prime2=str(i)
        while prime!='' and int(prime) in prime_list:
                prime = prime[:-1]
        if prime == '':
            while prime2!='' and int(prime2) in prime_list:
                prime2 = prime2[1:]
            if prime2 == '':
                truncate.append(i)
print(sum(truncate))
