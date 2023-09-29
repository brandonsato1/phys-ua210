# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:33:23 2023

@author: Brandon Sato
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros
import time

runs = 5
runtimes = [0,0,0,0,0]
runtimes2 = [0,0,0,0,0]
for z in range(runs):
    N=10*z
    C = zeros([N,N],float)
    A = np.random.random((N, N))
    B = np.random.random((N, N))
    
    t0 = time.time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] += A[i,j]*B[k,j]
                
    t1 = time.time()
    runtimes[z]=t1-t0
    t2 = time.time()
    D = np.dot(A,B)
    t3 = time.time()
    runtimes2[z] = t3-t2
plt.plot(range(0,runs*10,10),runtimes)
plt.plot(range(0,runs*10,10),runtimes2)
