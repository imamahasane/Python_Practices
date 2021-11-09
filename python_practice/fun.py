#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 04:44:10 2019

@author: imam
"""

def beautify(text):
    return text + "!!!"

def make_line(func, words):
    return "Hello " + func(words)

print(make_line(beautify, "World"))
