# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:20:10 2023

@author: Brandon Sato
"""
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (x)*(x-1)

x=1
d=10**(-7)

dfdx = (f(x+d)-f(x))/d

print(dfdx)