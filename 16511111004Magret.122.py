# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:24:28 2019

@author: Pale
"""

import numpy
def numx(x):
    mmin=min(x)
    mmax=max(x)
    average=sum(x)/len(x)
    return mmin,mmax,average
numlist=[]
for i in range(0,11):
    numlist.append(round(numpy.random.rand(),2))

print(numlist)
num1,num2,num3=numx(numlist)
print("min=",num1,"max=",num2,"average=",round(num3,2))    