# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 04:56:53 2019

@author: ASUS
"""

def newName():
    fName = input("Please enter your first name: ")
    lName = input("Please enter your list name: ")
    cityName = input("Enter your city: ")
    stateName = input("Enter your state: ")
    
    print("Your Name Is :", fName +" " +lName)
    print("You live in:", cityName +", " + stateName)
    
newName()