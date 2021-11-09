T = int(input())
l = []
for i in range(T):
    N = int(input())
    
    if N >= 0 and N <= 15:
        fact = 1
        while N >= 1:
            fact *= N
            N -=1
        l.append(fact)
        
for j in range(len(l)):
    
    print(l[j])