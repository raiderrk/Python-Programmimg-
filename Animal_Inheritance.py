# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:26:04 2024

@author: Rahul Kumar
"""

class Animal:
    
    def eat(self):
        self.name="Animal"
        print("All animal will eat....")
        
class Dog(Animal):  #inherit the data from parent class 
     pass;
print("..........................Animal's Data.........................")
a=Animal();
a.eat();
print(a.name);

print("..........................Dog data................................")
d=Dog();
d.eat();
print(d.name)        