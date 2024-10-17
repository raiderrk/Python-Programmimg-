# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:01:31 2024

@author: Rahul Kumar
"""

class Index:
    
    def checkIndex(self):
        try:
            
            arr=[10,20,30,40,50]
            print(arr[5])
        except IndexError:
            print("given index is out of range")
        
        
    def display(self):
        
        print("I am a disolay method");
        
        
i=Index()
i.display() 
i.checkIndex()
i.display()      
    