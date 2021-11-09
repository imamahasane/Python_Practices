def namta(ls):
    n = 1
    while n <= 10:
        x = ls * n
        print(ls,'*',n,'=',x)
        n +=1
        
u = int(input())
namta(u)