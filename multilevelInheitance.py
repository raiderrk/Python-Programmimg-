# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:28:39 2024

@author: Rahul Kumar
"""

class Animal:
    def eat(self):
        print("eating.......");
        
    def sleep(self):
        print("sleeping");
        
class Dog(Animal):
      
     def bark(self):
         print("barking.......")
         
class babyDog(Dog):
   
      def weep(self):
          print("weeping........")
          
a=Animal();
a.eat();
a.sleep();

d=Dog();
d.eat() ;
d.bark();
d.sleep() ;

b=babyDog();
b.eat();
b.sleep();
b.bark();
b.weep()     