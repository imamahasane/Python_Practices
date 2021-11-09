# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:58:38 2020

@author: emama
"""

def add(a: int, b: int) -> int:
    print(a, type(a))
    print(b, type(b))
    c = a + b
    print(c, type(c))
    return

add(2, 3)