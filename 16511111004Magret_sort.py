# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:38:09 2019

@author: Pale
"""

a=int(input("Input first number:"))
b=int(input("Input second number:"))
c=int(input("Input third number:"))
if a>b:
    a,b=b,a;
if b>c:
    b,c=c,b;
if a>b:
    a,b=b,a;
    
print("Sorted list:",a,b,c)