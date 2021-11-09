# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 19:29:07 2019

@author: ASUS
"""

def fahr_to_cel2():
    tmp = int(input("Please enter a fahr valu: "))
    
    if tmp:
        newTmp = 5 * (tmp -32) / 9
        print("The Fahr.. valus is",tmp,"to convert Cel..",newTmp,end='')
        print("is the cel..")
fahr_to_cel2()