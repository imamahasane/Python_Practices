def shape(n):
    for i in range(n+1):
        a = ''
        for j in range(i):
            a += '*'
        print(a)
        
q = int(input("Please input your number: "))
a = shape(q)
