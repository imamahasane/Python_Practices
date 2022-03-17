n = int(input("Please input a integer number: "))

num = [1, 2]

for i in range(3, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.append(i)  
print(num)