# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 06:27:43 2024

@author: Rahul Kumar
"""

class Product:
    
 
    
    def ProdInformation(self):
       print("product Id is",self.prodId);  
       print("product Name is",self.prodName);
       print("product Dept is",self.prodPrice);
        
       
    def __init__(self,prodId,prodName,prodPrice):
        self.prodId=prodId;
        self.prodName=prodName;
        self.prodPrice= prodPrice;
             
    
p=Product(1,"laptop",500)
p.ProdInformation();          
