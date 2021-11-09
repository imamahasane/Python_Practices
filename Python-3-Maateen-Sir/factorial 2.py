n = int(input("Please enter your input: "))

temp = n

while n > 1:
    n -= 1
    temp = temp * n
    
print(temp)