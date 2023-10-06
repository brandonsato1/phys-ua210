# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:02:52 2023

@author: Brandon Sato
"""

import numpy as np
import matplotlib as plt
from gaussxw import gaussxw
def f(x):
    return 1/(a**4-x**4)
N=10
a=0
b=2
x,w=gaussxw(N)
xp = .5*(b-a)*x + .5*(b+a)
wp = .5*(b-a)*w
s=0
for k in range(N):
    s += wp[k]*f(xp[k])
print(s)