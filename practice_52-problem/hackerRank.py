# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:04:39 2019

@author: ASUS
"""


def average(array):
    x = set(arr)
    m = sum(x)
    re = m / len(x)
    
    return re

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print(result)