# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 05:00:07 2019

@author: ASUS
"""

def if_statement():
    a, b, c = 5, 0, 0
    
    if a > 0:
        print("a is positive number.")
        
    if b > 0:
        print("b is positive number.")
    else:
        print("b is not posittive number.")
        
    if c > 0:
        print("c is posittive number.")
    elif c < 0:
        print("c is not posittive")
    else:
        print("c must be zero.")
        
if_statement()
        
    