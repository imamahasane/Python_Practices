# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:28:59 2019

@author: ASUS
"""
def is_leap(year):
    leap = False
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               not leap
           else:
               leap
       else:
           not leap
    else:
       leap
    return 
   

year = int(input())
print(is_leap(year))