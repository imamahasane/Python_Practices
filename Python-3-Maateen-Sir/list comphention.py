#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:46:09 2020

@author: imam
"""

my_list = [i**2 for i in range(20) if i % 2 == 0]
print(my_list)

my = []
for ik in range(20):
    if ik % 2 == 0:
        aa = ik**2
        my.append(aa)
        
print(my)