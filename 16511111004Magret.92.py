# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:15:37 2019

@author: Pale
"""

import random
a=random.sample(range(0,100),40)
count=0
for x in a:
    if count%5==0:
        print()
    print(x,end=" ")
    count=count+1
print("\nEnd!")