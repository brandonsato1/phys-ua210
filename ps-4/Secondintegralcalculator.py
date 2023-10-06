# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:29:19 2023

@author: Brandon Sato
"""
import numpy as np
import matplotlib as plt

def integrate(a):
    total = 0
    N2=10
    points = np.linspace(0.01,a,num=N2)
    for x in range(N2-1):
        y1 = 1/((a**4-points[x]**4)**1/2)
        y2 = 1/((a**4-points[x+1]**4)**1/2)
        total += (y2+y1)/2*(points[x+1]-points[x])
    return total

m=1
N=20
totals = []
points = np.linspace(0,2,num=N)
for x in range(N):
    totals.append((8*m)**1/2*integrate(points[x]))
print(totals)