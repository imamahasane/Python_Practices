#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 01:16:51 2020

@author: imam
"""

def add(*avg):
    temp = 0
    
    for i in avg:
        temp += i
        
    return temp

a = add(1,2,3,4,5,6,7,8)
print(a)