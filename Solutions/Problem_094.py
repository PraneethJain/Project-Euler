from rich import print
from time import time

t1 = time()
x, y = 2, 1

a3 = 0
ans = 0

while True:
    a3 = 2 * x - 1
    if a3 > 10**9:
        break
    area3 = (x - 2) * y

    if a3 % 3 == 0 and area3 % 3 == 0 and a3 > 0 and area3 > 0:
        ans += a3 + 1

    a3 += 2
    if a3 > 10**9:
        break
    area3 = (x + 2) * y

    if a3 % 3 == 0 and area3 % 3 == 0 and a3 > 0 and area3 > 0:
        ans += a3 - 1

    x, y = 2 * x + 3 * y, 2 * y + x
print(ans)
print(f"Process completed in {time()-t1} seconds")
