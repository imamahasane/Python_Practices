
T = int(input())
l = []
for i in range(T):
    N = input()
    if len(N) == 5:
        s = int(N[0]) + int(N[4])
        l.append(s)
        
for j in range(len(l)):
    print('Sum =',l[j])