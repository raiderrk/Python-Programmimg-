# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:56:14 2024

@author: Rahul Kumar
"""

from abc import ABC,abstractmethod

class Switch(ABC):
    
    
    @abstractmethod 
    def switchOn(self):
        pass;
        
   
    def display(self):
        print("Display.....")
       
#sw=Switch()  #In abstract method we can't create object of        
class Light(Switch):
    
    

    def switchOn(self):
        print("I am switchin on the light");
        
        
l=Light()
l.switchOn()    
l.display()        