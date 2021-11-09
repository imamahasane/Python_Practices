
print('\nWelcome To Your Normal Calculetor.')
print('1. __Addition')
print('2. __Subtraction')
print('3. __Multiplication')
print('4. __Division')
print('5. __Square')
print('6. __Queab')
print('0. __Exit')

def main():
    while True:  
        operation = int(input('Please type in the math operation:'))
        
        if operation == 1:
            def addition(*a):
                a = map(int, input().split())
                tmp = 0
                for number in a:
                    tmp += number
                print(tmp)
                
            
        elif operation == 2:
            def subtraction(*b):
                tmp = 0
                for number in b:
                    tmp -= number
                print(tmp)
            subtraction(10, 18)
            
        elif operation == 3:
            def multiplication(*c):
                tmp = 0
                for number in c:
                    tmp *= number
                print(tmp)                
            
        elif operation == 4:
            def division(d):
                tmp = 0
                for number in d:
                    tmp /= number
                print(tmp)                 
            
        elif operation == 5:
            def square(e):
                tmp = 0
                for number in e:
                    tmp = tmp ** number 
                print(tmp)                 
            
        elif operation == 6:
            def queab(f):
                tmp = 0
                for number in f:
                    tmp = tmp ** number 
                print(tmp) 
            queab(5)                
            
        elif operation == 0:
            break
        
        else:
            print("Your input is wrong. Please try again.\n Thank you so much.")
            
                
#def addition(a, b, c=0, d=0):
#    return a+b+c+d
#def subtraction():
#    try:
#        
#    except
#    return
#    
#def multiplication():
#    try:
#        
#    except
#    return
#
#def division():
#    try:
#        
#    except 
#    return
#    
#def square():
#    try:
#        
#    except
#    return
#
#def queab():
#    try:
#        
#    except
#    return
#
#if __name__ == "__main__":
#va = int(input().split())

main()