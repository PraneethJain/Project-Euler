from sympy.ntheory import factorint
from rich.progress import track
from rich import print
from time import time

t1 = time()
sum = {}
for x in track(
    range(1, 1_000_000 + 1), "[red bold]Generating sum of factors[/red bold]"
):
    prime_fac = factorint(x)
    result = 1
    for prime in prime_fac:
        result *= (prime ** (prime_fac[prime] + 1) - 1) / (prime - 1)
    sum[x] = int(result - x)

chains = set()
seen = set()
for i in track(range(2, 1_000_000), "[red bold]Generating Chains[/red bold]"):
    num = i
    L = [num]
    while True:
        if num in seen:
            break
        seen.add(num)
        L.append(num)
        num = sum[num]
        if num > 10**6:
            break
        if num == 1:
            break
        if num in L:
            chains.add(frozenset(L[L.index(num) :]))


high = 0
for chain in chains:
    current = len(chain)
    if current > high:
        high = current
        ans = min(list(chain))

print(ans)
print(f"Process completed in {time()-t1} seconds")
