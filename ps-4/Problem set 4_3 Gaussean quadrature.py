# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:38:51 2023

@author: Brandon Sato
"""

from numpy import ones,copy,cos,tan,pi,linspace
def gaussxw(N):#taken from the gaussxw class on github

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

import numpy as np
import matplotlib.pyplot as plt
import math
n=5
def H(n,x):
    
    if n==0:
        return 1
    if n==1:
        return 2*x
    else:
        return 2*x*H(n-1,x)-2*(n-1)*H(n-2,x)
def phi(x):
    n=4
    return math.e**(-x**2/2)*H(n,x)/(np.sqrt(2**n*math.factorial(n)*3.14159**1/2))
def f(x):
    z=x/(1-x**2)
    return z**2*abs(phi(z))**2*(1+x**2)/((1-x**2)**2)
N=100
a=-1
b=1
x,w=gaussxw(N)
xp = .5*(b-a)*x + .5*(b+a)
wp = .5*(b-a)*w
s=0.0
for k in range(N):
    s += wp[k]*f(xp[k])
print("exp value: ",s, "rms: ",s**1/2)