# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 04:13:39 2020

@author: emama
"""

a, b, c = map(int, input().split())

if a > b and a > c:
    print('biggest',a)    
    
elif b > a and b > c:
    print('biggest',b)
    
else:
    print('biggest',c)