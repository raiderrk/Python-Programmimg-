# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:37:45 2024

@author: Rahul Kumar
"""

class Animal:
    
    def eat(self):
        print("Eating......");
        
        
class Dog(Animal):

    def bark(self):
        print("barking.......");
            
class Cat(Animal):

    def meaw(self):
        print("meawing.......");

a=Animal();
a.eat() 
d=Dog();

d.bark();
d.eat();
c=Cat();
c.meaw()
c.eat();           