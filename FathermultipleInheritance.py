# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:18:26 2024

@author: Rahul Kumar
"""

class Father:
    
    def cook(self):
        print(" Father:- cooking....");
        
    
    def drive(self):
        print("driving...");
        
class Mother:
     
      def cook(self):
          print(" Mother:- cooking....");
          
class Son(Father,Mother):

      def play(self):

          print("playing....");

s=Son();
s.cook()
s.drive()
s.play()          