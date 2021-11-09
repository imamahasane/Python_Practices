# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 07:15:51 2019

@author: Imam Ahasan
"""

n = int(input())

count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1
        
print("n = ", n, "count = ", count)