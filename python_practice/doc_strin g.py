#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 04:23:26 2019

@author: imam
"""

def greet(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

# What the fucntion does?
print(greet.__doc__)
# Make sense, now lets use it    
greet("Hello World")