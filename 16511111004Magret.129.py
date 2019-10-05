# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:17:17 2019

@author: Pale
"""

scorelst=[ ['Jack B.G',65],
['Allan M. D.',85],
['Tomcat D. W',75],
['Annes G. J',54],
['Sam A. B',76],
['Jobs. S.S.',87]
]


fo=open("studentscores.txt","w")
for i in scorelst:
    fo.write(i[0]+","+str(i[1])+"\n")
fo.close()
print("End!")