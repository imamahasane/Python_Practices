# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 03:32:06 2019

@author: Imam Ahasan
"""

T = int(input())

ascinding_list = []
number_of_item = []

for i in range(T):
    string_input = input()
    ascinding_string = sorted(string_input)
    ascinding_list.append(ascinding_string)    


for j in range(len(ascinding_string)):
    valu = ascinding_list.count(ascinding_string[j])
    number_of_item.append(valu)
    
    print(ascinding_list[j],"=",number_of_item[j])
