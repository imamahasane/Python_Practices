#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:06:44 2020

@author: imam
"""

#n = int(input('Please enter your input: '))
m = []
for n in range(1, 101):
    if n % 3 == 0 and n % 5 != 0:
        m.append(n)
        
print(m)