# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:58:57 2019

@author: Pale
"""

esdict={}
enword=input("english: ")
snword=input("sesotho: ")
while (enword!="#" and snword!="#"):
    esdict[enword]=snword
    enword=input("english: ")
    snword=input("sesotho: ")

print("0. Exit")
print("1. english to sesotho")
print("2. sesotho to english")
select=int(input("Convert to: "))
while(select!=0):
    if select==1:
        enword=input("input english word:")
        if enword in esdict.keys():
            print("% s=>  %s"% ( enword,esdict[enword]))
        else:
            print("No such english word in dictionary ")
    elif select==2:
        cnword=input("input sesotho word:")
        for eachkey in esdict.keys():
            if esdict[eachkey]==cnword:
                print("%s ==> %s " %( cnword,eachkey)  )
                break
        else:
            print("no such sesotho word (%s) in dictionary" % (cnword))
    
    print("0. Exit")
    print("1. english to sesotho")
    print("2. sesotho to english")
    select=int(input("Your select:"))
print("Goodbye")