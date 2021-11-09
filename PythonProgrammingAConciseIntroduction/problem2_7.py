# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 06:56:01 2019

@author: ASUS
"""

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    side1 = float(input("enter length of side one:"))
    side2 = float(input("enter length of side two:"))
    side3 = float(input("enter length of side three:"))
    s = .5*(side1+side2+side3)
    area = (s*(s-side1)*(s-side2)*(s-side3))**.5
    print("Area of a traingle with sides",side1, side2,side3, "is",area)
  