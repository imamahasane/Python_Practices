# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 04:24:24 2019

@author: Imam Ahasan
"""

"""

Set .discard(), .remove() & .pop()

"""

n = int(input())
sd = input().split()
s = set([int(x) for x in sd]) 
mm = int(input())
for _ in range(mm):
    
    ff = input().split()
    a = list(ff)

    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print(sum(s))