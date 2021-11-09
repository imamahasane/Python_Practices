# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:11:34 2019

@author: Imam Ahasan
"""

def is_leap(a):
    if a / 100 != 0 and a / 4 == 0:
        print("True")
      
    elif a / 100 == 0 and a / 400 == 0:
        print("True")
        
    else:
        print("False")
    

year = int(input())
print(is_leap(year))