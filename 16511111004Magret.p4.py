# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:32:00 2019

@author: Pale
"""

money,rate,year=eval(input("Enter money,rate,year:"))
a=money*((1+rate)**year)
print("Future money is:",a)
print("End!")