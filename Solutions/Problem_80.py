from sympy import sqrt,evalf
from fraction import square_check
from rich import print
from rich.progress import track
from time import time

def get_sum(n: int) -> float:
    x=sqrt(n).evalf(102)
    sum=0
    for num in str(x)[:-2]:
        try:
            sum+=int(num)
        except:
            continue
    return sum

t1=time()
ans=0
for n in track(range(1,101),description="[bold cyan]Processing[/bold cyan]"):
    if not square_check(n):
        ans += get_sum(n)

print(ans)
print(f'Process completed in {time()-t1}s')
