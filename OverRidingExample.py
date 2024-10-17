# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:37:34 2024

@author: Rahul Kumar
"""

class Father:
    
    def drink(self):
        print("he drink softdrinks");
        
class Son(Father):

    def drink(self):
        print("he drinks hot drinks");
        
s=Son()
s.drink()        