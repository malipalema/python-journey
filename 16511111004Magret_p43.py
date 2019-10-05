# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:42:45 2019

@author: Pale
"""

name=input("enter name:")
weight=float(input("enter weight:"))
height=float(input("enter height:"))
BMI=round(weight/(height**2),2)
if BMI<=18.5:
    print("%s is underweight" %(name))
elif (BMI>18.5) and (BMI<=23):
    print("%s is normal" %(name))
elif (BMI>23) and (BMI<=25):
    print("%s is overweight-At risk" %(name))
elif (BMI>25) and (BMI<=30):
    print("%s is overweight-moderately obese" %(name))
else:
    print("%s is overweight-severely obese" %(name))
    