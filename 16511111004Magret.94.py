# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:26:43 2019

@author: Pale
"""

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=[x for x in a if x%2==0]
c=[x for x in a if x%2!=0]
print("Even numbers: ",b)
print("Odd numbers",c)