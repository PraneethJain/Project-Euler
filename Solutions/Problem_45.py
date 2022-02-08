def triangular_check(t:int) -> bool:
    n=((8*t+1)**0.5-1)/2
    return n==int(n)

def pentagonal_check(p: int) -> bool:
    n = (1+(24*p+1)**0.5)/6
    return n==int(n)

k=0
n=2
while k<2:
    Hn=n*(2*n-1)
    if triangular_check(Hn) and pentagonal_check(Hn):
        print(Hn)
        k+=1
    n+=1
