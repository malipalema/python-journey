# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:17:38 2019

@author: Pale
"""

income=float(input("Enter Income:"))
familysize=int(input("Enter family size:"))
if (income>=500000):
    tax=income*0.3
    print("Tax =",tax)
if (income<500000) and (income>=100000):
    if(familysize>3):
        tax=income*0.15
        print("Tax =",tax)
    if(familysize<=3):
        tax=income*0.2
        print("Tax =",tax)
if (income<100000) and (income>=30000):
    if(familysize>=5):
        tax=income*0.05
        print("Tax =",tax)
    if(familysize>=3) and (familysize<5):
        tax=income*0.07
        print("Tax =",tax)
    if(familysize<3):
        tax=income*0.1
        print("Tax =",tax)
if (income<30000) :
    print("Not Tax!")
print("End!")
    
    
        