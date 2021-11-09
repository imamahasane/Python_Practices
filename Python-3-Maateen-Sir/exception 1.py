# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 01:21:05 2020

@author: emama
"""

try:
    with open('ki.txt', 'r') as my_file:
        c = my_file.read()
        print(c)
        
except:
    print("The File dose not exit.")