# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:24:39 2019

@author: Pale
"""

lista=[54,32,78,45,38,65,27,41] 
listb=[78,61,45,32,51]
print("List a=",lista)
print("list b=",listb)
for x in lista:
    for n in listb:
        if x==n:
            lista.remove(x)
print("After Deletion:")
print("lista= ",lista)
