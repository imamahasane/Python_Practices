
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 04:36:02 2019

@author: Imam Ahasan
"""

for i in range(2, 30):
    j = 2
    count = 0
    
    while j < i:
        if i % j == 0:
            count = 1
            j += 1
            
        else:
            j += 1
            
    if count == 0:
#        print(str(i) + " is prime number.")
        print("%s is prime number." %str(i))
        
    else:
        count = 0