# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:17:03 2019

@author: Pale
"""

namelist=["Zhang","Wang","Deng","Weng","Zheng","Wu","Lin"]
print(namelist)
name1=input("Enter name in list: ")
name2=input("Enter name to be replacement: ")
n=namelist.index(name1)
namelist[n]=name2
print(namelist)