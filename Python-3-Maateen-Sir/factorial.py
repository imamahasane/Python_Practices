# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 05:21:38 2020

@author: emama
"""

n = int(input("Please enter your input: "))
temp = n

while n > 1:
    n -= 1    
    temp = temp * n   
    
print(temp)