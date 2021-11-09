
def spam(divideBy):
    global sk
    try:
        sk = 42 / divideBy
    
    except ZeroDivisionError:
        print("Error: Invalid argument.")
        
    return sk
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))