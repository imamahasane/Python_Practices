# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:17:27 2019

@author: ASUS
"""

from itertools import permutations

s, k = input().split()
rr = list(permutations(sorted(s),int(k)))
for i in rr:
    print(''.join(i))


