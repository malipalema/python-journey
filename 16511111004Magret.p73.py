# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:06:02 2019

@author: Pale
"""
num=1
for row in range(1,10):
    for col in range(1,10): 
        num=row*col
        if num < 10:
            empty = "  "
        else:
            if num < 100: 
                empty  = " " 
        if col == 0:
            if row == 0:
                print("    ", end = '')
            else:
                print("  ", row, end='')
        elif row == 0:
            print("  ", col, end='')
        else:
            if row>=col:
                
                print(empty, num, end = '')
    print()
    print(end="")
print("End!")