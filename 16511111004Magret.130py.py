# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:27:32 2019

@author: Pale
"""

def funct(x):
    n=0
    for i in range(1,5):
        if x[i]<60:
            n+=1
    return n
fo=open("marks.txt","r")
list=[]
for x in fo:
    x=x.split()
    list.append([str(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),0,0])
fo.close()
i=0

for i in list:
    sum1=x[1]+x[1]+x[3]+x[4]
    pass1=funct(x)
    list[i][5]=sum1
    list[i][6]=pass1
    i+=1
    
fo.open("studentmarks.txt","w")
hdr="{:<15} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format("Name","Mark1","Mark2","Mark3","Mark4","Total","Faild")
fo.write(hdr+"\n")
for x in list:
    st="{:<15} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(x[0],x[1],x[2],x[4],x[5],x[6])
    fo.write(st+"\n")
fo.close()
print("End!")

