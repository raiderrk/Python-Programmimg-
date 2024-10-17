# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:50:24 2024

@author: Rahul Kumar
"""

class Arithmetic:
    
    def divide(self,a,b):
        try:
            
           q=a/b;
           print(q);
           
        except ZeroDivisionError:
            
            print("Don't divide the number by zero");
            
    def display(self):
        print("I am just a method");
        
a=Arithmetic();
a.display()
a.divide(10, 0)      
a.display()  
         
         