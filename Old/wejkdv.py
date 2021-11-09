# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:41:39 2019

@author: ASUS
"""

from itertools import permutations
N = int(input())
K = input().split()
a = int(input())

m = tuple(permutations(K, a))

print(m+N/len(m))