#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 01:00:15 2020

@author: imam
"""

n = input('Please enter a any input: ')

k = n[::-1]

if n == k:
    print("Palindom")
    
else:
    print("Not Palindom")