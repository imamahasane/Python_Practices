# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:01:02 2019

@author: ASUS
"""

def inches_to_feet2(inches):
    feet = inches // 12
    extra_inches = inches % 12
    print(inches, "inches is", feet, "feet and", extra_inches, "inches")
inches_to_feet2(77)