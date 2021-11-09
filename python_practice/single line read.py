# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:43:36 2020

@author: emama
"""

with open("file.text", "r") as fp:
    lines = fp.readlines()
    print(lines)
    for line in lines:
        print(line)