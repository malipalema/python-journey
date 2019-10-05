# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:08:32 2019

@author: Pale
"""
import cmath 

a=int(input("Input a:"))
b=int(input("Input b:"))
c=int(input("Input c:"))
d=(b**2)-(4*a*c)
x=-b/(2*a)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

if d<0:
    print("Two different roots:".sol1,sol2)
    
if d==0:
    print("Identical roots: %.2f,%.2f",x, x)
    
if d>0:
    print('Image roots {0} {1}'.format(sol1,sol2))
print("End!")


    