
def spam():
    global eggs
    eggs = "spem"    #this is the global
    
    
def becon():
    eggs = "becon"    #this is a local
    
    
def ham():
    print(eggs)    #this is the global
    
    
eggs = 42    #this is the global

spam()
print(eggs)

    