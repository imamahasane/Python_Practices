
ans = 0
neg_flg = False

x = int(input("Enter an integer: "))

if x < 0:
    neg_flg = True
    
while ans ** 2 < x:
    ans += 1
    
# note    
    
    