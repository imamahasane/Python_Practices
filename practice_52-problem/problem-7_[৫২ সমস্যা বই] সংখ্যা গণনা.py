T = int(input())

l = []

for i in range(T):
    N = input()
    x = N.split(' ')
    m = len(x)
    l.append(m)
    
for j in range(len(l)):
    print(l[j])