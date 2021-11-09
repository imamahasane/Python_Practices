# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:37:14 2019

@author: Imam Ahasan
"""

if __name__ == "__main__":
    y = int(input())
    
def divition(a):
    if a / 100 != 0 and a / 4 == 0:
        print("True")
#        
#    elif a / 100 == 0:
#        print("False")
        
    elif a / 100 == 0 and a / 400 == 0:
        print("True")
        
    else:
        print("False")
        
divition(y)