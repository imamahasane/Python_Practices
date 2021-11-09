# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:13:43 2019

@author: ASUS
"""

for i in range(2, 30):
    j = 2
    count = 0
    
    while j < i:
        if i % j == 0:
            count = 1
            j +=1
            
        else:
            j += 1
            
    if count == 0:
        print("%s is a prime number."%str(i))
        
    else:
        count = 0