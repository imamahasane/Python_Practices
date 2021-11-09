#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:24:54 2020

@author: imam
"""

a = [i for i in range(11)]
print('A =',a)
b = [i for i in range(11, 21)]
print('B =',b)

c = zip(a, b)
print('C =',c)

print(list(c))

