# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:37:48 2019

@author: Pale
"""


def pi(n):
    total=0
    sign=-1
    for i in range(1,n+1):
        sign*=-1
        total += sign * ( 4 / (2*i - 1)  )     
    print(total)
n = int(input("Enter number of terms: "))
pi(n)

