# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:17:30 2019

@author: Pale
"""

def check(x):
    oo=0
    pp=0
    x=x.split()
    for i in x:
        for j in i:
            j=ord(j)
            if 47<j<58:
                oo+=1
            elif 64<j<91 or 96<j<123:
                pp+=1
    return oo,pp
a=input("ENTER STRING= ")
x,y=check(a)
print("numbers= ",x,"letter= ",y)

