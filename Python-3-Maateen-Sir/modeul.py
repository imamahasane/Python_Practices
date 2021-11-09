# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:40:14 2020

@author: emama
"""

import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Level")
plt.plot(history.history['loss'])