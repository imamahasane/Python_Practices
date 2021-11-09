#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 01:37:31 2020

@author: imam
"""

def c(n):
    print(n)
    n += 1
    c(n)
    
c(1)