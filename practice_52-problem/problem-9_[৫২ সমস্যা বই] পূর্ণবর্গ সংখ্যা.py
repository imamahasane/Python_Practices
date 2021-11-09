import math

T = int(input())
l = []
m = []
for i in range(T):
    N = int(input())
    m.append(N)

    x = math.sqrt(N)
    x = int(x)
    l.append(x)
    
for j in range(len(l)):
    
    if m[j] == l[j]*l[j]:
        print('YES')
            
    else:
        print('NO')