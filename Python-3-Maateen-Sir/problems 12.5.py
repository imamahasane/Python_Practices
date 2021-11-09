#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:34:09 2020

@author: imam
"""

n = [1,1,1,11,3,1,13, 62, 33,11, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99]

m = []
for i in n:
    if i not in m:
        m.append(i)
print(m)