# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:47:52 2024

@author: Rahul Kumar
""";

class Customer:
    CategoryOfCustomer="Wholeseller"
    
    def __init__(self):
        self.nameOfCustomer="John"  #instance variable
        print(self.nameOfCustomer)
        
    def purchase(self):
        print(self.nameOfCustomer,"purchace household items")
        
    @classmethod 
    def FindTypeOfCust(cls):
            print(cls.CategoryOfCustomer)
            
    @staticmethod 
    def pay():
            print(Customer.CategoryOfCustomer) #indirect class data
            c1=Customer();
            print(c1.nameOfCustomer) # indiect object method
            print("I ama static method")

c=Customer();
Customer.pay();
c.purchase();            