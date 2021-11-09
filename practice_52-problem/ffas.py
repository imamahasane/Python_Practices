# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:32:51 2019

@author: ASUS
"""
year = int(input())
def is_leapyear(year):
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("{0} is a leap year".format(year))
           else:
               print("{0} is not a leap year".format(year))
       else:
           print("{0} is a leap year".format(year))
    else:
       print("{0} is not a leap year".format(year))
return 