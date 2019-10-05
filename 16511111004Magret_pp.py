# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:25:42 2019

@author: Pale
"""

name=input("Type your name: ")
print('Hi, I have seen you before:'+name.upper()+'!\n')

len_name=len(name)
print("The length of your name is:"+str((len_name))+'\n')

name_f3=name[0:3]
print('The first 3 letters of your name are: '+name_f3.upper()+'\n')

name_l3=name[-3:]
print('The last 3 letters in your name are: '+name_l3.upper()+'\n')
print("Goodbye!")