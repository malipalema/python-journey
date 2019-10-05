# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:11:52 2019

@author: Pale
"""

def isPrime(x):
    if x>1:
        for i in range(2,x):
            if(x%i)==0:
                return False
                break
        else: 
            return True
    else: 
        return False

for j in range(100,999):
    if isPrime(j):
        print(j,end=" ")
print()
x,y=eval(input("Enter x,y: "))
count=0
for k in range (x,y):
    if isPrime(k):
        count+=1

print("number of prime numbers is= ",count)

       
        
        
            