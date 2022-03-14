
n = int(input("Please input a integer number: "))

for i in range(2, n):
    if n % i == 0:
        print(f'{i}, not a prime number')
        break
    
    else:
        print(f'{n}, a prime number')
        break
   
else:
    print(f'{n}, is not a prime number')
    
for i in range(n):
    for j in range (i+1):
        if j % 2 == 0:
            print("*", end="")
        
        else:
            print('#', end="")
        
    print('\n')