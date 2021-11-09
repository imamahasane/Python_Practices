# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:05:18 2020

@author: emama
"""

a = int(input("Please enter input an integer number: "))

if a < 10:
    if a % 2 == 0:
        print("Less, yes")
        
    else:
        print("Less, no")
        
else:
    if a % 3 ==0:
        print("Greater, yes")
        
    else:
        print("Greater, no")