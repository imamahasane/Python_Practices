# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 04:40:42 2019

@author: Imam Ahasan
"""

n = int(input())
s = set()
for i in range(n):
    stamp_input = input()
    s.add(stamp_input)
    
print(len(s))
