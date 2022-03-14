from prime import primelist, primecheck
from itertools import product
from time import time


def thingy(p1: int, p2: int) -> bool:
    return primecheck(int((str(p1) + str(p2)))) and primecheck(int(str(p2) + str(p1)))


# ATTEMPT 2 (FASTER)
t1 = time()
prime_list = set(primelist(10**4))
for p1, p2 in product(prime_list, repeat=2):
    if p2 > p1:
        if thingy(p1, p2):
            for p3 in prime_list:
                if p3 > p2:
                    if thingy(p1, p3) and thingy(p2, p3):
                        for p4 in prime_list:
                            if p4 > p3:
                                if thingy(p1, p4) and thingy(p2, p4) and thingy(p3, p4):
                                    for p5 in prime_list:
                                        if (
                                            thingy(p1, p5)
                                            and thingy(p2, p5)
                                            and thingy(p3, p5)
                                            and thingy(p4, p5)
                                        ):
                                            print(p1 + p2 + p3 + p4 + p5)
                                            print(f"Process completed in {time()-t1}s")
                                            raise SystemExit


# ATTEMPT 1 (TAKES YEARS, SHOULD STILL WORK)
# t1=time()
# prime_list=primelist(10**4)
# for p1,p2,p3,p4,p5 in product(prime_list,repeat=5):
#     if p5>p4>p3>p2>p1:
#         if all(thingy(a,b) for a,b in product([p1,p2,p3,p4,p5],repeat=2)):
#             print(sum([p1,p2,p3,p4,p5]))
#             print(f'Process completed in {time()-t1}s')
#             raise SystemExit
