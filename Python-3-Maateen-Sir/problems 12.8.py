#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 01:12:13 2020

@author: imam
"""

u = int(input('Please enter your input: '))
n = [1, 11, 3, 13, 62, 33, 9, 12, 18, 21, 24,3,3, 27, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99]

mm = []
for valu in n:
    if valu == u:
        mm.append(valu)
        
print('Fount', len(mm), 'time.')

        
