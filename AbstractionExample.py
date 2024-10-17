# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:40:57 2024

@author: Rahul Kumar
"""

from abc import ABC,abstractmethod

class Switch(ABC):
    
    @abstractmethod 
    def switchOn(self):
        pass;
       
        
class Light(Switch):

    def switchOn(self):
        print("I am switchin on the light");
        
        
l=Light()
l.switchOn()    
        