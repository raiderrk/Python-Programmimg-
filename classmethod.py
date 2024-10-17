# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:44:22 2024

@author: Rahul Kumar
"""

class Customer: # class declartion
    @classmethod   # class method decorater
    def purchase(cls): # class method
        print(cls)

Customer.purchase();  #print the class Name            