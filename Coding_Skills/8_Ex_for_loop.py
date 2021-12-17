"""
5. Write a program that prints following shape

*
**
***
****
*****

"""
for i in range(1, 6):
    a = ''
    for j in range(i):
        a += '*'
    
    print(a)

# OR

n = int(input("Please inter your input: "))

for i in range(1, n+1):
    m = ''
    for j in range(i):
        m += '*'
    print(m)
        



    