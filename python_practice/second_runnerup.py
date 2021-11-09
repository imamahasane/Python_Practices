# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 05:42:05 2019

@author: Imam Ahasan
"""

def second_runnerup(v):
    remove_duplicat = sorted(set(v))
    result = remove_duplicat[-2]
    return result

if __name__ == "__main__":
    n = int(input())
    a = map(int, input().split())
    ok = second_runnerup(a)
    print(ok)