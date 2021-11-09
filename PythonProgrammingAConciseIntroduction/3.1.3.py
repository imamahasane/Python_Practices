# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 07:05:07 2019

@author: ASUS
"""

def fah_to_cel3():
    tmp = input()
    if tmp:
        if tmp.isdigit():
            tmp = int(tmp)
            newTmp = 5 * (tmp - 32) / 9
            print(newTmp)
            
        else:
            print("You most enter a number. bye")
            
fah_to_cel3()