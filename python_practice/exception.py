# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:53:00 2020

@author: emama
"""

def div(a, b):
    try:
        return a / b
    
    except ZeroDivisionError:
        print("Can't divide by zero")
        
    except TypeError:
        print("Unsupported type. Did you use string.")

print(div(10, 2))
print(div(3, 0))
print(div(9, 3))
print(div('12', 3))