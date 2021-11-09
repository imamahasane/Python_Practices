# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:46:36 2019

@author: emama
"""

m_list = []
T = int(input())

if T >= 1 and T <= 25:
    for i in range(T):
        N = int(input())
        m_list.append(N)
        
    if N >= 1 and N <= 80:
        for i in range(len(m_list)):
            for j in range(m_list[i]):
                print('*'*m_list[i])
            if i == (len(m_list) -1):
                break
            else:
                print()