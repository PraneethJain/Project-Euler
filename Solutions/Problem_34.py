from math import factorial as f
L=[]
for x in range(10,1_000_000):
    s = sum(f(int(i)) for i in list(str(x)))
    if s==x:
        L.append(x)
print(L)
print(sum(L))
