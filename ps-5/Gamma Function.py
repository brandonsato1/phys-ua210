# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:16:34 2023

@author: Brandon Sato
"""

import numpy as np
import matplotlib.pyplot as plt
p = [2,3,4]

#Integrand
def f(x):
    return x**(a-1)*np.e**(-x)

#Changed of variables integrand
def f2(x):
    #return (np.e**(np.log(x)*(3/2-1)*-x))
    return ((np.e**(np.log(x)))**(a-1)*np.e**(-x))

for a in p:
    graph = []
    xvalues = np.linspace(0,5,num=1001)
    for x in xvalues:
        graph.append(f(x))
    plt.plot(xvalues,graph)
    plt.xlabel("x")
    plt.ylabel("y")
    #print("Max value for a = " , a , " found at:" ,  xvalues[graph.index(max(graph))], ". a-1 =" ,a-1)
    
def gamma(a):
    c=2*(a-1)/(a-1)
    totalcount = 0
    intvalues = np.linspace(0.000001,.999999,num=999)
    for z in intvalues:
        totalcount += ((np.e**(np.log(z*c/(1-z))))**(a-1)*np.e**(-z*c/(1-z)))*(c/((1-z)**2))*(intvalues[1]-intvalues[0])
    return totalcount



#print("Gamma = ", gamma(3/2))

print("Gamma(3) = ", gamma(3) , "Gamma(6) = ", gamma(6) , "Gamma(10) = ", gamma(10))