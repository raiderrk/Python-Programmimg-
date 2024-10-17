# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:39:41 2024

@author: Rahul Kumar
"""

d1={1:'a','cd':45.6,3:'John'}


for k in d1:
    
    print(k,"--> key")
    print(d1[k],"-->value")
    
    
d2={1:'a','cd':45.6,3:'John'}
print(d2)    


d={1:'a',2:'b',3:'c',4:'d'}

d.popitem()
print(d)


s={1:'a',2:'b',3:'c',4:'d'}

s.setdefault(2,4)
print(s)

s1={1:'a',2:'b',3:'c',4:'d'}

#s1.update(1,"a")
print(s1)


ss={1:'a',2:'b',3:'c',4:'d'}

ss.values()
print(ss)