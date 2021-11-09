#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:27:06 2020

@author: imam
"""

n = [3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99]

my_list = []

for i in n:
    if i <= 60:
        my_list.append(i)
        
print(my_list)