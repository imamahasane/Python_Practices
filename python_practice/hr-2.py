# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:19:05 2019

@author: Imam Ahasan
"""

n = int(input())

if n >= 1 and n <= 100:
    if n % 2 != 0:
        print("Weird")
        
    elif n >= 2 and n <= 5:
        if n % 2 == 0:
            print("Not Weird")
            
    elif n >= 6 and n <= 20:
        if n % 2 == 0:
            print("Weird")
            
    elif n > 20:
        if n % 2 == 0:
            print("Not Weird")
