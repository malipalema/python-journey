# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:32:06 2019

@author: Pale
"""

def exponential(n,x):
    sum=1
    for i in range(n,0,-1):
        sum=1+x*sum/i
    print("e(x) is about= ",sum)
n=int(input("Enter the nth term: "))
x=int(input("Enter a number: "))
exponential(n,x)