# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:09:46 2019

@author: Pale
"""

import cmath
from math import sqrt
a = float(input('Please enter a : '))
b = float(input('Please enter b : '))
c = float(input('Please enter c : '))
x=-b/(2*a)
delta = (b**2) - (4*a*c)
solution1 = (-b-cmath.sqrt(delta))/(2*a)
solution2 = (-b+cmath.sqrt(delta))/(2*a)
sol1 = (-b-sqrt(delta))/(2*a)
sol2 = (-b+sqrt(delta))/(2*a)
if a!=0:
    
    if delta>0:    
        print('Image roots {0} and {1}'.format(solution1,solution2))
    
    if delta<0:
        print("Two different real roots:".sol1,sol2)
    
    if delta==0:
        print("Identical roots:",x, x)
    print("End!")
    