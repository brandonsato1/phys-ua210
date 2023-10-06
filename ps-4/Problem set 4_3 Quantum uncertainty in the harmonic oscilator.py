# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:08:18 2023

@author: Brandon Sato
"""
import numpy as np
import matplotlib.pyplot as plt
def H(n,x):
    
    if n==0:
        return 1
    if n==1:
        return 2*x
    else:
        return 2*x*H(n-1,x)-2*(n-1)*H(n-2,x)
    """
points = np.linspace(-4,4,num=20)
n=4
for z in range(n):
    li = []
    for x in points:
        li.append(H(z,x))
    plt.plot(np.linspace(-4,4,num=20),li)
    """
li2 = []
points2 = np.linspace(-10,10,num=20)
for x in points2:
    li2.append(H(30,x))
plt.plot(np.linspace(-10,10,num=20),li2)