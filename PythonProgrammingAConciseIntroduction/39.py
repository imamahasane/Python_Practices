# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 07:34:13 2019

@author: ASUS
"""

def absolutevalue(num):
    if num >= 0:
        abs_num = num
        
    else:
        abs_num = -num
        
    print("This absolutevalue value of", num, "is", abs_num)
    
absolutevalue(5)
absolutevalue(-5)
absolutevalue(4-4)