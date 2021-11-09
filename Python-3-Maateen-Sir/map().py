# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 01:22:50 2020

@author: emama
"""

m_list = [1, 2, 3, 4, 5, 6, 7]

def square(x):
    return x * x

n_list = map(square, m_list)
print(n_list)
print(list(n_list))