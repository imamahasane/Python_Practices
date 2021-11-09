T = int(input())

l = []   
for i in range(T):
    r1, r2, r3 = input().split()
    r1 = int(r1)
    r2 = int(r2)
    r3 = int(r3) 
    
    pb = 300-r3
    crr = (r2 / pb) * 6
    arr = ((r1 - r2 + 1) / r3) * 6
    
    tmp = []
    tmp = "%.2f"%crr,"%.2f"%arr
    
    l.append(list(tmp))
    
for j in range(len(l)): 
    print(" ".join(l[j]))