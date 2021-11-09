
def framge(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
for i in framge(0.5, 1.0, 0.1):
    print(i)