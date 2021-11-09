# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:38:01 2020

@author: emama
"""

import sys

print(sys.argv)
print(type(sys.argv))

arguments = sys.argv

a = arguments[1]
b = arguments[2]
 
print(a + b)
