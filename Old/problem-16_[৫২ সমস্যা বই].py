# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:41:58 2019

@author: emama
"""

T = int(input())

l = []

for i in range(T):
    N = input()
    x = N.split(' ')
    
    l.append(N)
    
for j in l:
    print(j[0][::])
    