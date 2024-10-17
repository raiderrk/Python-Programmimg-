# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:11:18 2024

@author: Rahul Kumar
"""


n=int(input("Enter No:="))

print("4th Questions")

for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(i,end=" ")
        
        
        
    print()    
    
print("5th questions")    


for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
        
    
        
    print()      
    
    
    
print("6th questions")    

x=64
for i in range(1,n+1):
    for j in range(i):
        print(chr(i+x),end=" ")
        
    
    print()    

    
    
print("7th questions")    

x=64
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(chr(j+x),end=" ")
        
    
    print()    
    
print("8th questions")

for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(chr(i+64),end=" ")
        n=n+1
    print()    
    
    
    
    
    
# print("9th questions")    

# x=64
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(chr(i+x),end=" ")
        
    
#     print()       
    