T = int(input())

l = []

for i in range(T):
    N = input().split()
    
    if len(N) == 3:
        
        N.sort()
        l.append(N)
        
count = 0
for j in range(len(l)):
    count += 1
    print("Case",count,":",' '.join(l[j]))