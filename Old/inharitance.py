# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:47:23 2019

@author: ASUS
"""

class Parent:
    def __init__(self):
        print("This is the parent class")
        
    def parentFunc(self):
        print("This is the parent func")
#        
#p = Parent()
#
#p.parentFunc()

class Child(Parent):
    def __init__(self):
        print("This is chile class")
        
    def childfunc(self):
        print("This is chaild func")
        
c = Child()
c.childfunc()
c.parentFunc()
