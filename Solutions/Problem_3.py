import math


x = int(input("Enter a positive Integer: "))
factors = []
prime = []
for i in range(1,math.ceil(x/2+1)):
  if x % i == 0 :
    factors.append(i)
factors.append(x)
print(factors)
for x in factors:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        prime.append(x)
print(max(prime))
input('Press ENTER to exit')
