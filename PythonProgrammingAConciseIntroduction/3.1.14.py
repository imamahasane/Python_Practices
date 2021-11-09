# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:15:09 2019

@author: ASUS
"""
#%%
def count_by_5():
    print("Counting from 5 through 100 in  steps of 5")
    ct = 5
    while ct < 101:
        print(ct, end=" ")
        ct += 5
    print()
count_by_5()
#%%
def count_by_5():
    print("Counting from 5 through 100 in  steps of 5")
    for ct in range(5, 101, 5):
        print(ct, end=" ")
    print()
    
count_by_5()
#%%
