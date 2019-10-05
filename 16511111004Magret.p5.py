# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:59:05 2019

@author: Pale
"""

n=int(input("Enter any even number: "))
total=0
for number in range(1,n+1):
    if (number%2==0):
        total=total+number
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))
print("End!")