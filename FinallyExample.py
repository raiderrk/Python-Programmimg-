# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:44:30 2024

@author: Rahul Kumar
"""

class Calculation:
    
    def division(self,a,b):
        
        c=None;
        
        try:
            c=a//b;
            
            
        except:
            print("Denominator must be zero");
            
        finally:
            print("finally:-- num can be zero but denom cannot be zero")
            
        print(c);
        
        
c=Calculation();
c.division(10,2)        
        