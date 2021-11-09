# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 01:17:29 2020

@author: emama
"""

import re

my_string = "purple alice@gmail.com, blah monkey bob@abc.con blah dishwasher"
temp = my_string.split(',')

for ph in temp:
    result = re.search("([\w\.-]+)@([\w\.-]+)", ph)
    print(result.group())
