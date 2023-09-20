# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:33:51 2023

@author: Brandon Sato
"""

import numpy as np
from matplotlib import pyplot as plt

M_set_x = []
M_set_y = []
notM_set_x = []
notM_set_y = []
N=100
for x in range(-200,200,2):
    for y in range(-200,200,2):
        c = complex(float(x)/100,float(y)/100)
        z=complex(0,0)
        for count in range(N):
            z = z*z + c
        if abs(z) <= 2:
            M_set_x.append(x/100)
            M_set_y.append(y/100)
        elif abs(z) > 2:
            notM_set_x.append(x/100)
            notM_set_y.append(y/100)
        else:
            print("Something went wrong at",x,y,z)
                
plt.scatter(M_set_x,M_set_y)