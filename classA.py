# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:48:03 2024

@author: Rahul Kumar
"""

class A:
    def display(self):
     print(" I am in a class A");
        
class B(A):
    
    def show(self):
        print("I am in a class B");
        
class C(A):
    
     def show(self):
         print("I am in a class c");
         
class D(B,C):
     
     def present(self):
         print("I am in a class D");

d=D();
d.display();
d.show();
d.present();         
             