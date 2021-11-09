#%%

def problem1_1():
    print("Problem Set 1")
    
problem1_1()

#%%

def problem1_2(x,y):
    print(x + y)
    
problem1_2(3, 5)

#%%

def problem1_3(n):
    li =[]
    m = 1
    while m <= n:
        li.append(m)
        m += 1
    print(sum(li))
        
problem1_3(6)

#%%

def problem1_4(miles):
    print("There are", (5280 * miles), "feet in",miles, "miles.")
problem1_4(5)

#&&

def problem1_5(age):
    if age < 7:
        print("Have a glass of milk.")
    elif age < 21:
        print("Have a coke.")
    else:
        print("Have a martini.")
problem1_5(5)
problem1_5(10)
problem1_5(25)

#%%

def problem1_6():
    for i in range(1, 100, 2):
        print(i, end=" ")
    print()
problem1_6()

#%%

def problem1_7():
    a = int(input("Enter the length of one of the bases: "))
    b = int(input("Enter the length of the other base: "))
    c = int(input("Enter the height: "))
    result = ((1/2)*(a+b)) * 12
    result = float(result)
    print("The area of a trapezoid with bases", float(a), "and", float(b), "and height", float(c), "is",result)
problem1_7()

#&&