# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:02:53 2019

@author: Pale
"""

from calendar import monthrange
month=int(input("Enter Month number: "))
year=int(input("Enter year: "))
print(monthrange(year,month))
