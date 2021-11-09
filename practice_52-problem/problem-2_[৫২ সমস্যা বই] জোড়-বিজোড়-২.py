# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:43:32 2019

@author: emama
"""

T = int(input())

for i in range(0, T):
    n = input()
    n = int(n)
    
    if (n % 2 == 0):
        print("even")
        
    else:
        print("odd")