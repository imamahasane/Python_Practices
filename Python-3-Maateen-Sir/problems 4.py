#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:03:12 2020

@author: imam
"""

n = input("Please enter the input: ")

if n >= 'a' and n <= 'z':
    print("Lower Cass")
    
elif n >= 'A' and n <= 'Z':
    print("Upper Cass")
    
else:
    print("Nothing")