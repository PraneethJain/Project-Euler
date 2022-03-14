from time import time


def triangular_check(t: int) -> bool:
    n = ((8 * t + 1) ** 0.5 - 1) / 2
    return n == int(n)


def square_check(s: int) -> bool:
    n = s**0.5
    return n == int(n)


def pentagonal_check(p: int) -> bool:
    n = (1 + (24 * p + 1) ** 0.5) / 6
    return n == int(n)


def hexagonal_check(h: int) -> bool:
    n = (1 + (8 * h + 1) ** 0.5) / 4
    return n == int(n)


def heptagonal_check(h: int) -> bool:
    n = (3 + (40 * h + 9) ** 0.5) / 10
    return n == int(n)


def octagonal_check(o: int) -> bool:
    n = (2 + (12 * o + 4) ** 0.5) / 6
    return n == int(n)


t1 = time()
octagonal_nums = [i for i in range(10**3, 10**4) if octagonal_check(i)]
all_set = set(
    [
        i
        for i in range(10**3, 10**4)
        if any(
            [
                triangular_check(i),
                square_check(i),
                pentagonal_check(i),
                hexagonal_check(i),
                heptagonal_check(i),
                octagonal_check(i),
            ]
        )
    ]
)
listoflists = []
for n1 in octagonal_nums:
    for n2 in all_set:
        if str(n1)[-2:] == str(n2)[:2]:
            for n3 in all_set:
                if str(n2)[-2:] == str(n3)[:2]:
                    for n4 in all_set:
                        if str(n3)[-2:] == str(n4)[:2]:
                            for n5 in all_set:
                                if str(n4)[-2:] == str(n5)[:2] and str(n5)[2] != "0":
                                    n6 = int(str(n5)[-2:] + str(n1)[:2])
                                    listoflists.append([n1, n2, n3, n4, n5, n6])
for L in listoflists:
    ans = 0
    for ele in L:
        if heptagonal_check(ele):
            ans += ele
            L.remove(ele)
    for ele in L:
        if hexagonal_check(ele):
            ans += ele
            L.remove(ele)
    for ele in L:
        if pentagonal_check(ele):
            ans += ele
            L.remove(ele)
    for ele in L:
        if square_check(ele):
            ans += ele
            L.remove(ele)
    for ele in L:
        if triangular_check(ele):
            ans += ele
            L.remove(ele)
    if len(L) == 1:
        print(ans + L[0])
        print(f"Process completed in {time()-t1}s")
        raise SystemExit
