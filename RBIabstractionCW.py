# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:12:23 2024

@author: Rahul Kumar
"""

from abc import ABC,abstractclassmethod

class RBI(ABC):
    
    @abstractclassmethod 
    def provide_loan(self):
        pass
    
    def display(self):
        print("Anything")
    
class Axis(RBI):

    

    def provide_loan(self):
        print("Axis bank provide the loan amount is Rs 10000000")
        
        
class Hdfc(RBI):

    def provide_loan(self):
        print("HDFC bank provide the loan amount is Rs 20000000")



h=Hdfc()
h.provide_loan()


a=Axis();
a.provide_loan()        
a.display()

            
        