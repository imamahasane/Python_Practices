# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 04:44:09 2019

@author: ASUS
"""

def userName():
    fName = input("Please enter the first name: ")
    lName = input("Please enter the last name: ")
    
    fullName = fName +" "+ lName
    return fullName

print(userName())


def userName():
    fName = input("Please enter the first name: ")
    lName = input("Please enter the last name: ")
    
    return fName +" " + lName

print(userName())