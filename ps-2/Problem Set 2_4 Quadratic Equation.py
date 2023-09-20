# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:14:37 2023

@author: Brandon Sato
"""

a = float(input("Input value of a: "))
b = float(input("Input value of b: "))
c = float(input("Input value of c: "))

x1 =( -b + (b**2-4*a*c)**(1/2))/(2*a)
x2 = ( -b - (b**2-4*a*c)**(1/2))/(2*a)

print("Roots are",x1,x2)


x_1 = (2*c)/(-b-(b**2-4*a*c)**(1/2))
x_2 = (2*c)/(-b+(b**2-4*a*c)**(1/2))


print("Using second equation, roots are",x_1,x_2)
print("Fixed: ", (round(x1)),(round(x2)))