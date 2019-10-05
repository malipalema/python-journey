# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:29:03 2019

@author: Pale
"""

def isLeapyear(x):
    if x%4==0 and x%100!=0 or x%400==0:
        return True
    else: 
        return False

def days(a,b):
    ordinary=[21,28,31,30,31,30,31,31,30,31,30,31]
    leap=[21,29,31,30,31,30,31,31,30,31,30,31]
    if isLeapyear(a):
        return leap[b-1]
    else:
        return ordinary[b-1]
    
def past(y,m,d):
    numdays=0
    for i in range(1,m):
        numdays+=days(y,i)
    return numdays
    
x,y,z=eval(input("Enter year,month,day: ")) 
print("passed days",past(x,y,z))
    
    
    


    