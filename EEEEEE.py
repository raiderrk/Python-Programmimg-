# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:25:10 2024

@author: Rahul Kumar
"""

class Vehicle:
    
    def __init__(self,model,brand):
        
        self.model=model
        self.brand=brand
        
class car(Vehicle):

     def __init__(self, model, brand ,manufactureYear,color):
         
         super().__init__(model, brand)
         self.manufactureYear=manufactureYear
         self.color=color
         
        
c=car("TOYOTO","Etios",2023,"red");
print(c.model)
print(c.brand)
print(c.manufactureYear)
print(c.color)
       
         
         