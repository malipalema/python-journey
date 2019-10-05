# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:21:01 2019

@author: Pale
"""
import math
def sin(x,n):
    sine = 0
    for i in range(n):
        sign=(-1)**i
        pi=22/7
        y=x*(pi/180)
        sine=sine+((y**(2*i+1))/math.factorial(2*i+1))*sign
    return sine
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(sin(x,n))        