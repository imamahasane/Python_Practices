n = int(input("Please input a integer number: "))

num = [1, 2]

for i in range(3, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.append(i)    

for i in num:
    print(f"{i} :", end='')
    for j in range(i):
        if j % 2 == 0:
            print("*", end="")
        
        else:
            print("#", end="")
        
    print('\n')

