ter_prog = False

while not ter_prog:
    n1 = int(input('Please enter a number: '))
    n2 = int(input('Please enter another number: '))
    
    while True:
        oper = input("Please enter add/sub or quit to exit: ")
        
        if oper == 'quit':
#            ter_prog = True
            break
        
        if oper not in ['add', 'sub']:
            print('Unknow Operator')
            continue
        
        if oper == 'add':
            print('The result is: ',n1+n2)
            
        
        if oper == 'sub':
            print('The result is: ',n1-n2)