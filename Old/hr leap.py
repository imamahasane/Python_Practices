# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:16:09 2019

@author: ASUS
"""

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
       if year % 100 == 0:
           if year % 400 == 0:
               not leap
           else:
               leap
       else:
           not leap
    else:
        leap
    
    return leap

year = int(input())
print(is_leap(year))