# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:13:30 2024

@author: Rahul Kumar
"""

def getSmall(num):
    
    small=9
    
    while num!=0:
        
        digit=num%10
         
        
        if digit<small:
            
            small=digit
        num=num//10
    return small

n=int(input("Enter the No:"))

print(getSmall(n))     


        
       
       