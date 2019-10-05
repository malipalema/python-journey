# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:55:20 2019

@author: Pale
"""

marks=[]
dataSet=int(input("number of datasets= "))
for x in range(0,dataSet):
    name=input("Enter name: ")
    com,eng,chin,math=eval(input("input marks= "))
    total=com+eng+chin+math
    marks.append([name,com,eng,chin,math,total])
print("%-10s %-10s %-10s %-10s %-10s %-10s"%("Name","Computer","English","Chinese","Maths","Total"))

for i in range(len(marks)):
    print("%-10s %-10s %-10s %-10s %-10s %-10s"%(marks[i][0],marks[i][1],marks[i][2],marks[i][3],marks[i][4],marks[i][5]))
max=marks[0][5]
temp=0
for j in range(len(marks)):
    if marks[0][5]>max:
        temp=j
print("Highest total= ",marks[temp][0])

for k in marks:
    if k[1]<50 or k[2]<50 or k[3]<50 or k[4]<50:
        print()
print("students who have failed at least one course: ",k[0],end=" ")

    
    
