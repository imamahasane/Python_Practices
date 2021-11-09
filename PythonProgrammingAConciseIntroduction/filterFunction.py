# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:27:06 2019

@author: ASUS
"""

def is_even(x):
    return x % 2 == 0

my_numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, my_numbers)
print(list(result))
