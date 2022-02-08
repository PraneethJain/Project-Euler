from fractions import Fraction
L=[Fraction(3/2)]
def approx(x):
    if x==0:
        return Fraction(3,2)
    else:
        L.append(1+Fraction(1,(1+L[x-1])))
        return 1+Fraction(1,(1+L[x-1]))

ans = 0
for i in range(1000):
    x = approx(i)
    if len(str(x.numerator)) > len(str(x.denominator)):
        ans += 1
print(ans)
