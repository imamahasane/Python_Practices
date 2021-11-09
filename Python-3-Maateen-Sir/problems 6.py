#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:50:08 2020

@author: imam
"""

n = int(input("Please enter your input: "))
m = n

temp = n // 1000
print(temp, "1000 takar note(s)")

if temp > 0:
    n = n % 1000
    m = n
    
else:
    n = m


temp = n // 500
print(temp, "500 takar note(s)")

if temp > 0:
    n = n % 500
    m = n
    
else:
    n = m
    

temp = n // 100
print(temp, "100 takar note(s)")

if temp > 0:
    n = n % 100
    m = n
    
else:
    n = m
    

temp = n // 50
print(temp, "50 takar note(s)")

if temp > 0:
    n = n % 50
    m = n
    
else:
    n = m


temp = n // 20
print(temp, "20 takar note(s)")

if temp > 0:
    n = n % 20
    m = n
    
else:
    n = m


temp = n // 10
print(temp, "10 takar note(s)")

if temp > 0:
    n = n % 10
    m = n
    
else:
    n = m
    
    
temp = n // 5
print(temp, "5 takar note(s)")

if temp > 0:
    n = n % 5
    m = n
    
else:
    n = m
    
    
temp = n // 2
print(temp, "2 takar note(s)")

if temp > 0:
    n = n % 2
    m = n
    
else:
    n = m
    
    
temp = n // 1
print(temp, "1 takar note(s)")

if temp > 0:
    n = n % 1
    m = n
    
else:
    n = m

    