# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:38:26 2019

@author: emama
"""

l = []

T = int(input())

for i in range(T):
    N = int(input())
    l.append(N)
c = 1
for i in l:
    print("case {}: ".format(c), end="")
    print(' '.join(str(j) for j in range(1, i+1) if i%j==0 ))
    c+=1