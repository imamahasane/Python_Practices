# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:44:59 2019

@author: emama
"""

A = 1000

while True:
    x = A - 5
    
    for i in range(A, x, -1):
        print(i, end = "\t")
        
    print()
    
    A = x
    
    if A <= 0:
        break