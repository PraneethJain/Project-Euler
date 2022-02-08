#(3n^2-n)/2=P --> n=(1+sqrt(24p+1))/6
def pentagonal_check(p: int) -> bool:
    n = (1+(24*p+1)**0.5)/6
    return n==int(n)


j=1
while True:
    for k in range(1,j):
        pj=int(j*(3*j-1)/2)
        pk=int(k*(3*k-1)/2)
        if pentagonal_check(pj+pk) and pentagonal_check(pj-pk):
            print(pj-pk,pj,pk)
            break
    j += 1
