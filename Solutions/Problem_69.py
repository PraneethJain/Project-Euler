from time import time
from prime import primelist

t1 = time()
prime_list = primelist(20)
product = 1
i = 0
while product * prime_list[i] < 10**6:
    product *= prime_list[i]
    i += 1
print(product)
print(f"Process completed in {time()-t1}s")

# from sympy import totient as phi
# high=0
# ans=0
# for i in range(10**5,10**6):
#     current=i/phi(i)
#     print(i)
#     if current>high:
#         high=current
#         ans=i
# print(ans)
