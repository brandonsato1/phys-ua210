# -*- coding: utf-8 -*-
"""
Calculation for Madelung Constant
Created on Mon Sep 18 16:56:42 2023

@author: Brandon Sato
"""

import numpy as np
from matplotlib import pyplot as plt

#Loop version
L = 100
M = 0
for i in range(-L,L,1) :
    for j in range(-L,L,1):
        for k in range(-L,L,1):
            if i==0 and j==0 and k == 0:
                print("0,0,0")
            elif (i+j+k) % 2 == 0:
                M -= 1./((i**2+j**2+k**2)**(1./2))
            elif (i+j+k) % 2 == 1:
                M += 1./((i**2+j**2+k**2)**(1./2))
            else: 
                print("Something went wrong at",i,j,k,M)
print("Madelung Constant:",M)


#Sum version
L=100
M=0
i = np.array(range(-L,L,1))
j = np.array(range(-L,L,1))
k = np.array(range(-L,L,1))

M=sum(1./((i**2)))