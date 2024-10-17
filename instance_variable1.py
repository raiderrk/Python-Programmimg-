# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:59:09 2024

@author: Rahul Kumar
"""

class Bike:
    color ="Red"; #class vaiable
    
    def __init__(self):
        self.price=1000;#instance variable

b= Bike();
print(Bike.color)
print(b.price)        