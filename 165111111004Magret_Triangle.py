# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:49:38 2019

@author: Pale
"""
from math import sqrt
print("Enter 3 sides")
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
if (a+b>c) and (a+c>b) and (b+c>a):
    L=(a+b+c)/2
    area=sqrt(L*(L-a)*(L-b)*(L-c))
    print("Yes these numbers can make a triangle the area is:",area)
else:
    print("No, this sides cannot make a triangle")
print("End!")