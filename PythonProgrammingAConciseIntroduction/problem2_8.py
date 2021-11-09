# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 06:56:11 2019

@author: ASUS
"""

def problem2_8(temp_list):
    sum = 0
    for temp in temp_list:
        sum += temp
    avg = sum/len(temp_list)
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    print("Average:",avg)
    print("High:",max_temp)
    print("Low:",min_temp)