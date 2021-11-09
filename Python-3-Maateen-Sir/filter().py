# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 04:09:40 2020

@author: emama
"""

m_list = [1, 2, 3, 4, 5, 6, 7]

def is_even(x):
    if x % 2  == 0:
        return True
    
    else:
        return False

n_list = filter(is_even, m_list)
print(n_list)
print(list(n_list))