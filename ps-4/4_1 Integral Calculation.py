# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 23:34:01 2023

@author: Brandon Sato
"""
import numpy as np
N1 = 10
N2 = 20
p1 = 0
p2 = 2
points = np.linspace(p1,p2,num=N1,dtype=float)
points2 = np.linspace(p1,p2,num=N2,dtype=float)
total = 0
total2 = 0
for x in range(N1-1):
    y1 = (points[x]**4 - 2*points[x] + 1)
    y2 = (points[x+1]**4-2*points[x+1]+1)
    total += (y1+y2)/2 * (points[x+1]-points[x])
print("Total with 10 points: ",total)

for x in range(N2-1):
    y1 = (points2[x]**4 - 2*points2[x] + 1)
    y2 = (points2[x+1]**4-2*points2[x+1]+1) 
    total2 += (y1+y2)/2 * (points2[x+1]-points2[x])
print("Total with 20 points: ",total2)

print("Error is:" ,abs( total2-total)*1/3)