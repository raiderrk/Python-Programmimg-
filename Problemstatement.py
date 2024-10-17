# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:06:31 2024

@author: Rahul Kumar
"""

class InsufficentStockError(BaseException):
    pass

class ProductNotInOrderError(BaseException):
    pass

class OrderCannotBeFulfilledError(BaseException):
    pass


class Product:
    
    def __init__(self,name,price,quantityInstock):
        self.name=name;
        self.price=price
        self.quantityInstock=quantityInstock
        
    def updateStock(self,update):
       self.update=update;
      
    def getInfo():    
        pass
    
class Order:

    def __init__(self,oid):
        self.oid=oid
        self.product={}
        
    def addProduct(self,addProduct):
        self.addProduct=addProduct
        
    