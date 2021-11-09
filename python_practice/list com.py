# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 03:59:03 2019

@author: Imam Ahasan
"""

if __name__== "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(result)