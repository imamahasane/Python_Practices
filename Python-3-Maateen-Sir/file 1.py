# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 00:29:34 2020

@author: emama
"""

my_file = open('test.txt', 'r')
content = my_file.read()
print(content)
my_file.close()