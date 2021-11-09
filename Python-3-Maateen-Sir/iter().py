# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:06:41 2020

@author: emama
"""

class revrange:
    
    def __init__(self, n):
        self.n = n
        self.i = n
        
    def __iter__(self):    #iter() Itarabol object pass krahoi
        return self
    
    def __next__(self):    #next() Iteratir er poroborti item access krar jnno
        if self.n >= 0:
            if self.i == self.n:
                self.n = self.n - 1
                return self.i
            
            else:
                self.i = self.n
                self.n = self.n - 1
                return self.i
        else:
            raise StopIteration
            
for temp in revrange(5):
    print(temp )