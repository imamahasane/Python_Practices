# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 07:02:24 2019

@author: Imam Ahasan
"""

n = 100
even = [False] * (n+1)

for i in range(0, n+1, 2):
    even[i]  = True
    
print(even[2])
print(even[3])