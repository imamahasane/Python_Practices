# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 05:12:49 2019

@author: emama
"""

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("enter length of side one:"))
    b = float(input("enter length of side two:"))
    c = float(input("enter length of side three:"))
    s = (a + b + c) / 2
    print("Area of a triangle with sides {:.1f} {:.1f} {:.1f} is {:.1f}".format(a, b, c, (s * (s - a) * (s - b) * (s - c)) ** 0.5))