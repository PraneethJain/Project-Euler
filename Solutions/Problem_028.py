from time import time

# center to top right: (2n+1)^2
# center to top left: (2n+1)^2-2n
# center to bottom left:(2n+1)^2-4n
# center to bottom right:(2n+1)^2-6n
t1 = time()
print(sum((4 * ((2 * n + 1) ** 2) - 12 * n) for n in range(1, 501)) + 1)
print(f"Process completed in {time()-t1}s")
