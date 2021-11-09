
def spam():
    eggs = "spam local"
    print(eggs)    #print 'spam local'
    
    
def bacon():
    eggs = "bacon local"
    print(eggs)    #print 'bacon local'
    
    spam()
    print(eggs)    #print 'bacon local'
    
    
eggs = "global"    #print 'global'
bacon()
print(eggs)
    
    