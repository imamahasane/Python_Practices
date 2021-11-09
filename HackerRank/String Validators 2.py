# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 01:58:51 2020

@author: emama
"""

if __name__ == '__main__':
    s = input()

    print(any(a.isalnum() for a in s))
    print(any(a.isalpha() for a in s))
    print(any(a.isdigit() for a in s))
    print(any(a.islower() for a in s))
    print(any(a.isupper() for a in s))