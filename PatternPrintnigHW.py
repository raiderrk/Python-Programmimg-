# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:54:53 2024

@author: Rahul Kumar
"""

n= int(input("Enter the number: \n"));
d=69
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(chr(d),end=" ")
        d=d-1
        if d==64:
            d=69
        else:
            continue

            
    print()
    

print("************* 2nd way***************" )   


for i  in range(1,n+1):

    for j in range(n,0,-1):
        print(chr(j+64),end=" ")
        
    print()    
    

print("2nd Questions")    
        
    
for i  in range(n,0,-1):

    for j in range(n,0,-1):
        print(chr(i+64),end=" ")
        
    print() 

print("3rd Questions") 

for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(i,end=" ")
        
    print()    
    
    
    
print("3rd Questions another way")    


for i in range(n):
    for j in range(i):
        print(i,end=" ")
        n=n-1
        
    print()    
    
 
    
  
    
        
    
   