# Replace VIIII to IX then IIII to IV
# Replace LXXXX to XC then XXXX to XL
# Replace DCCCC to CM then CCCC to CD

from rich import print
from time import time

t1 = time()
with open(r"files\p089_roman.txt") as f:
    file = f.readlines()
file = [ele.strip() for ele in file]

ans = 0
for roman in file:
    if "VIIII" in roman:
        ans += 3
    elif "IIII" in roman:
        ans += 2
    if "LXXXX" in roman:
        ans += 3
    elif "XXXX" in roman:
        ans += 2
    if "DCCCC" in roman:
        ans += 3
    elif "CCCC" in roman:
        ans += 2

print(ans)
print(f"Process completed in {time()-t1} seconds")
