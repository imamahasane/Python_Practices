# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:46:46 2019

@author: ASUS
"""

def inchesto_feet(inches):
    feet = inches // 12
    extra_inches = inches - (12  * feet)
    print(inches, "inches is", feet, "feet and", extra_inches, "inches.")
    
inchesto_feet(77)