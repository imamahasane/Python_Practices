# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 06:13:17 2019

@author: ASUS
"""

import random

def problem2_4():
    L = []
    random.seed(70)
    for n in range(0,10):
        L.append(random.random()*5 + 30)
    print(L)
