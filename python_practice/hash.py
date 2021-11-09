# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:22:45 2019
3713081631934410656
@author: Imam Ahasan
"""

my_tuple = ()
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    re = my_tuple + tuple(integer_list)

    print(hash(re))


