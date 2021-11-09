#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:50:22 2020

@author: imam
"""

n = int(input("Plese enter your date of birthday: "))

if 4 % n == 0 and 100 % n != 0:
    print("Lepyer")
    
elif 100 % n == 0 and 400 % n == 0:
    print("Lepyer")
    
else:
    print("Not Lepyer")