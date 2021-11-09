# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 07:22:59 2019

@author: Imam Ahasan
"""

def count_substring(string, sub_string):
    re = list(string)
    sas = re.count(sub_string)
    return sas

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
