# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:33:56 2019

@author: Pale
"""

x=int(input("Enter 3 digit number: "))
sum=0
temp=x
while temp>0:    
    a=temp%10
    sum += a**3
    temp //=10

if x==sum:
    print(x,"Is a Narcissistic number")
else:
    print(x,"Is not a Narcissistic number")
    