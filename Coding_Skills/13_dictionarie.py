def shape(a = 7):
    for i in range(a+1):
        m = ''
        for j in range(i):
            m += '*'
        print(m)
    
    for i in range(a+1, 0, -1):
        n = ''
        for j in range(i):
            n += '*'
        print(n)
    return 
# re = int(input("Please input hear: "))
v = shape()

print(v)