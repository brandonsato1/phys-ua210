# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:17:33 2023

@author: Brandon Sato
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import random

s=10000
Nbi = 10000
Nbi209 = 0
Nti = 0
Npb = 0
tau = 0

for i in range(s):
    for z in range(Npb):
        tauPb = 3.3*60
        pPb = 1-2**(-1/(tauPb))
        if random.rand()<pPb:
            Npb-=1
            Nbi209 +=1
    for x in range(Nbi):
        tauBi = 46*60
        pBi = 1-2**(-1/(tauBi))
        if random.rand()<pBi:
            if random.rand()<.9791:
                Npb +=1
                Nbi -=1
            else:
                Nti +=1
                Nbi -=1
    for y in range(Nti):
        tauTi = 2.2*60
        pTi = 1-2**(-1/(tauTi))
        if random.rand()<pTi:
            Npb += 1
            Nti -= 1
    
print(Nti, Npb, Nbi, Nbi209)
            
            