# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:07:53 2019

@author: Imam Ahasan
"""

def integer_division(a, b):
    result = a // b
    return result

def float_division(a, b):
    result = a / b
    return result

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    
ob = integer_division(a, b)
ob2 = float_division(a, b)

print(ob)
print(ob2)