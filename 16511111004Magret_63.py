# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 08:27:37 2019

@author: Pale
"""

def pi(n):
    for i in range(1,n,7):
        total = (((1)/(i+i+1))-((1)/(i+i+2))+((1)/(i+i+4)))

    value = 4*(1-total)
    print(value)
n = int(input("Enter the value of n: "))
pi(n)

