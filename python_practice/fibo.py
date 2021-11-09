def find_fibo(n):
    if n <= 2:
        return 1
    fibo_x, fibo_next = 1, 1
    
    i = 3
    while i <= n:
        i += 1
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
    return fibo_next

for m in range(1, 11):
    print(find_fibo(m))
    
    
def list_fibo(n):
    fibo_list = [1, 1]
    if n <= 2:
        return fibo_list[:n]
    fibo_x, fibo_next = 1, 1
    
    i = 3
    while i <= n:
        i += 1
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
        fibo_list.append(fibo_next)     
    return fibo_list

for a in range(1, 11):
    print(find_fibo(a))

print(list_fibo(1))
print(list_fibo(2))
print(list_fibo(10))
