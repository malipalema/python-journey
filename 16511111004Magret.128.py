# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:07:44 2019

@author: Pale
"""

scores=[ 65,87,89,92,76,82,61,53,45,78,98,72,83,69,72,51,83,87,64,52,96,64,72,69,79,65,54,34,65,86,76,43,96,96,76]
fo=open("p1.txt","w")
for i in scores:
    fo.write(str(i)+"\n")
fo.close()
print("end!")