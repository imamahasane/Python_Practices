# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 04:20:25 2019

@author: Imam Ahasan
"""

def fib(n):
    serise = []
    a, b = 0, 1
    
    while b < n:
        serise.append(b)
        a, b = b, a+b
        
    return serise

if __name__ == "__main__":
    tmp = fib(100)
    print(tmp)
    