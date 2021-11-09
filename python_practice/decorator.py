# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:09:59 2019

@author: emama
"""

def my_decorator(func):
    def decorator():
        print("-----------")
        func()
        print("-----------")
    return decorator

def print_row():
    print("Clear Text")
    
deco_func = my_decorator(print_row)
deco_func()