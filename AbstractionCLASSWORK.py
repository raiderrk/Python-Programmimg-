# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:03:43 2024

@author: Rahul Kumar
"""

from abc import ABC,abstractclassmethod

class Shape(ABC):
    
    def __init__(self):
        self.radius=None;
        self.side=None;
        self.length=None;
        self.breadth=None;
        
    @abstractclassmethod 
    def Find_Area(self):
        pass;
       
        
class Circle(Shape):

    def Find_Area(self,r):
        self.radius=r;
        
        return self.radius*self.radius*3.14

class Square(Shape):

    
    def Find_Area(self,side):
        self.side=side;
        return self.side*self.side
    
s=Square()
print(s.Find_Area(2))

c=Circle()
print(c.Find_Area(1));   
        
    
        
        