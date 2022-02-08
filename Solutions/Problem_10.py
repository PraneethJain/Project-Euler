import math


l = math.floor(float(input("Enter lower limit: ")))
u = math.ceil(float(input("Enter upper limit: ")))
print("Printing primes between",l,"and",u)
primes = []
if u>l and l>0:
  for x in range(l,u+1):
    for i in range(2,x):
      if x%i==0:
        break
    else:
      if x == 1:
        continue
      else:
        print(x)
        primes.append(x)
else:
  print("Bad Input")
print(sum(primes))
input('Press ENTER to exit')