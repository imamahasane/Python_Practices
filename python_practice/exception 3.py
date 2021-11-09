# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 02:35:54 2020

@author: emama
"""

import io

filename = "file.txt"
mode = "r"

try:
    with open(filename, mode) as fp:
        content = fp.read()
        
except FileNotFoundError:
    print(filename, "not found.")
    
except io.UnsupportedOperation:
    print("Are you sure", filename, "is readable.")