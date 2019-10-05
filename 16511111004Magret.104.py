# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:44:40 2019

@author: Pale
"""

dict1={0:'Zero',1:'One',2:'Two',3:'Three',4:'four',\
5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

n=input("Enter number= ")
for i in n:
    print( dict1[ord(i)-48],end=" ")
print()