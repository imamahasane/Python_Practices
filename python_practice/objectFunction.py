#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 04:36:56 2019

@author: imam
"""

def ad(line):
    return line + "!"
print(ad("Hi Imam"))
update_ad = ad
print(update_ad("Hi Imam"))
print(update_ad)