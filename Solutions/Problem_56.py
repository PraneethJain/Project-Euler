current = None
high = 0
for a in range(1,100):
    for b in range(1,100):
        current=sum(list(map(int,list(str((a**b))))))
        if current>high:
            high = current
print(high)