# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 00:33:16 2020

@author: emama
"""

my_file = open('imam.txt', 'r')
c = my_file.read()
print(c)
my_file.close()