# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:01:18 2024

@author: Rahul Kumar
"""
print('****************a|(b&c)*******************88')

a={1,2,3,4,5,6}
b={5,6,7,8}
c={1,4,8,9}

s=b.intersection(c)
s1=a.union(s)
s1=a|b & c
print(s1)

print("**********************a|(b-c)*****************")

a1={1,2,3,4,5,6}
b1={5,6,7,8}
c1={1,4,8,9}

s2=a1.union(b1.difference(c1))
print(s2) 


print("***********************a&(b-c)********************")

a2={1,2,3,4,5,6}
b2={5,6,7,8}
c2={1,4,8,9}

s3=a1.intersection(b.difference(c))
print(s3)