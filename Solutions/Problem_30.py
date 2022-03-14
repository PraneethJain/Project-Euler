from time import time

t1 = time()
print(
    sum(
        i for i in range(2, 5 * (9**5)) if i == sum(int(j) ** 5 for j in list(str(i)))
    )
)
print(f"Process completed in {time()-t1}s")
