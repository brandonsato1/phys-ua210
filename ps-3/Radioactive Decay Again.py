# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:23:53 2023

@author: Brandon Sato
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

N=1000
s=1000
e=2.81
tau=3.05*60
mu=-np.log(2/tau)
times = []
for y in range(s):
    t=-1/mu*np.log(1-random.rand())
    times.append(t)
    
np.sort(times)
print(times)

  
# getting data of the histogram
count, bins_count = np.histogram(times, bins=10)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(bins_count[1:], cdf, label="times")
plt.legend()