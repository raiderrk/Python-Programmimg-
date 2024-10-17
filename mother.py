# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:28:09 2024

@author: Rahul Kumar
"""

class Father:
    
    def cook(self):
        print(" Father:- cooking...."); 
        
    
    def drive(self):
        print("driving...");
        
class Mother:
     
      def cook(self):
          print(" Mother:- cooking...."); # if same properties have both super
                                          #  class mother as well as father 
                                          # then sub class prefare which super class inherit first by the sub class (Son).
          
class Son(Mother,Father):                 # then sub class prefare which super class inherit first by the sub class (Son).


      def play(self):

          print("playing....");

s=Son();
s.cook()
s.drive()
s.play()          