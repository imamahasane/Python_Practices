# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:11:47 2019

@author: ASUS
"""

def make_double(x):
    return x * 2

my_marks = [10, 12, 20, 30]
result = map(make_double, my_marks)
print(list(result))
