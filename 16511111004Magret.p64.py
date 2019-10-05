# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:56:47 2019

@author: Pale
"""

nterms=int(input("Enter the nth term: "))
n1 = 1
n2 = 1
count = 0
##print("Fibonacci sequence upto",nterms,":")
for row in range(1,11):
    for col in range(1,11):
        num=row*col
        print(num,end=" ")
    nth = n1 * n2
    n1 = n2
    n2 = nth
    count += 1
    
