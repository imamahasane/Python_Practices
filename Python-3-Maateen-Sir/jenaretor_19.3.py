
def revrange(n):
    while n >= 0:
        yield n
        n -= 1
        
for temp in revrange(5):
    print(temp)