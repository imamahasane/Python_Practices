# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 07:17:10 2019

@author: ASUS
"""

def area(type_, x):
    if type_ == "circle":
        area = 3.14*x**2
        print(area)
        
    elif type_ == "sqare":
        area = x **2
        print(area)
        
    else:
        print("I don't know that one")
        
area("circle", 5)
area("sqare", 8)        
area("manai", 7)