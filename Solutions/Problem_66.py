from math import sqrt
from fractions import Fraction
from time import time


def square_check(x: int) -> bool:
    return (int(x**0.5)) ** 2 == x


def cont_frac(x: int) -> list:
    L = []
    m = 0
    d = 1
    a = int(sqrt(x))
    L.append(a)
    while a != 2 * int(sqrt(x)):
        m = d * a - m
        d = (x - m**2) / d
        a = int((sqrt(x) + m) / d)
        L.append(a)
    return L + L[1:]


def convergents(x: int) -> list:
    L = cont_frac(x)
    frac_list = [Fraction(L[0], 1), Fraction(L[1] * L[0] + 1, L[1])]
    for i in range(2, len(L)):
        frac_list.append(
            Fraction(
                frac_list[i - 2].numerator + L[i] * frac_list[i - 1].numerator,
                frac_list[i - 2].denominator + L[i] * frac_list[i - 1].denominator,
            )
        )
    return frac_list


def min(D: int) -> int:
    if square_check(D):
        return 0
    else:
        for convergent in convergents(D):
            x = convergent.numerator
            y = convergent.denominator
            if x**2 - D * (y**2) == 1:
                return x


t1 = time()
current = 0
high = 0
for D in range(1, 1001):
    current = min(D)
    if current > high:
        high = current
        ans = D
print(ans)
print(f"Process completed in {time()-t1}s")
