# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:27:02 2020

@author: emama
"""

lines = ["This is the first line", "This is the second line", "This is the third line"]

with open("file.text", "w") as fp:
    for line in lines:
        fp.write(line+"\n")