T = int(input())

l = []
p = []

def reverse(string): 
    string = string[::-1] 
    return string

for i in range(T):
    N = int(input())
    
    if N >= 0 and N <= 10000:
        fact = 1
        while N >= 1:
            fact *= N
            N -=1
        m = str(fact)
        
        l.append(reverse(m))

count = 0
#        print(l)
for k in l: 
    for n in k:           
        if n == '0':
            count += 1
        else:
            break
    p.append(count)
        
for j in range(len(p)):
    print(p[j])