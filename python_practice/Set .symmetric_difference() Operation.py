# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 07:29:00 2019

@author: Imam Ahasan
"""

a = int(input())
a_input = set(map(int, input().split()))
    
b = int(input())
b_input = set(map(int, input().split()))
    
print(len(a_input.symmetric_difference(b_input)))