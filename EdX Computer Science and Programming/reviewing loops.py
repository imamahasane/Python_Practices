
ans = 0
neg_flg = False

x = int(input("Enter an integer: "))

if x < 0:
    neg_flg = True
    
while ans ** 2 < x:
    ans += 1
    
if ans ** 2 == x:
    print(f"Square root of {x} is {ans}")
    
else:
    print(f"{x} is not a perfect square")
    
    if neg_flg:
        print(f"Just checking... did you mean {-x} ?")
    