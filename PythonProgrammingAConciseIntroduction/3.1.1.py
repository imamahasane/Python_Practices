# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 19:13:39 2019

@author: ASUS
"""

def fahr_to_cel():
    temp = int(input("Enter a fahrentheit temperature: "))
    new_temp = 5 * (temp - 32) /9
    print("The fahrentheit temperature", temp, "is equiaent  to", end='' )
    print(new_temp,"degress celsius")
    
fahr_to_cel()