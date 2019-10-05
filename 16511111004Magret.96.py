# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:03:47 2019

@author: Pale
"""

s = []
n=int(input("s= "))
while n>0:    
    s=s+[n]
    n=int(input("s= "))
    a=[x for x in s if x>=90]
    b=[x for x in s if x>=80 and x<90]
    c=[x for x in s if x>=70 and x<80]
    d=[x for x in s if x>=60 and x<70]
    e=[x for x in s if x<60]
    a1=len(a)
    b1=len(b)
    c1=len(c)
    d1=len(d)
    e1=len(e)
    average=sum(s)/len(s)
print("max=",max(s),"min=",min(s),"ave=",round(average,2))
print("A= ",a1,"B= ",b1,"c= ",c1,"D= ",d1,"E= ",e1)