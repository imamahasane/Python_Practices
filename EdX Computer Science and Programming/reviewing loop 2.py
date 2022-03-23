
ans = 0
neg_flag = False

x = int(input("Enter an Integer Number: "))

if x < 0:
    neg_flag = True
    
while ans ** 2 < x:
    ans += 1
    
if ans ** 2 == x:
    print(f"Square root of {x} is {ans}")
    
else:
    print(f"{x} is not a perfect square")
    
    if neg_flag:
        print("Just checking... did you mean {-x} ?")