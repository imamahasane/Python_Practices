#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:11:47 2020

@author: imam
"""

n = input("Please enter a input: ")

if n >= 'a' and n <= 'z' or n >= 'A' and n <= 'Z':
    if n in 'aeiouAEIOU':
        print("Vowel")
        
    else:
        print("Consonant")
        
else:
    print("Nothing")