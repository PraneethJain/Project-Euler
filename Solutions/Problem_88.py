from rich import print
from time import time


def minimal_product_sum(product: int, sum: int, count: int, lower_limit: int) -> None:
    k = product - sum + count
    if k < 12000:
        ans_list[k] = product if product < ans_list[k] else ans_list[k]
    for fac in range(lower_limit, 24000 // product + 1):
        minimal_product_sum(product * fac, sum + fac, count + 1, fac)


t1 = time()
ans_list = [24000] * 12000
minimal_product_sum(1, 1, 1, 2)
print(sum(set(ans_list[2:])))
print(f"Process completed in {time()-t1} seconds")
