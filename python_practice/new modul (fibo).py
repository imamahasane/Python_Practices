# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 05:02:57 2019

@author: emama
"""

def find_fibo(n):
    if n <= 2:
        return 1
    fibo_x, fibo_next = 1, 1
    
    i = 3
    while i <= n:
        i += 1
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
    return fibo_next

for m in range(1, 11):
    print(find_fibo(m))
    