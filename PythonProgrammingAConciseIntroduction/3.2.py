# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 04:20:51 2019

@author: ASUS
"""

def far_to_cel(tmp):
    newTmp = 5 * (tmp - 32)/9
    print("The fahra temperature",tmp,"is equalent to",newTmp, end=' ')
    print("degree celsius")
    
far_to_cel(212)