from math import factorial as f


def ncr(n,r):
    return int(f(n)/(f(r)*f(n-r)))

ans = 0
for n in range(1,101):
    for r in range(0,n+1):
        if ncr(n,r)>10**6:
            ans +=1
print(ans)