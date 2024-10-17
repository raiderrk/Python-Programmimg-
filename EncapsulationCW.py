# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:52:10 2024

@author: Rahul Kumar
"""

class Customer:

    
    def __init__(self):
        
        self.__custId=None;
        self.__custName=None;
        self.__custContact=None;
        
    def getCustId(self):
        
        return self.__custId;
    
    def setCustId(self, cId):
        
        self.__custId=cId;
        
    def getCustName(self):
            
        return self.__custName;
        
    def setCustName(self,CName):
            
         self.__custName=CName;
          
    def getCustContact(self):
            
        return self.__custContact;
        
    def setCustContact(self,cContact):
            
        self.__custContact=cContact;
        
        
        
class Product:

    
    def __init__(self):
        
        self.__prodId=None;
        self.__prodName=None;
        self.__prodPrice=None;
        
    def getProdId(self):
        
        return self.__prodId;
    
    def setProdId(self, pId):
        
        self.__prodId=pId;
        
    def getProdName(self):
            
        return self.__prodName;
        
    def setProdName(self,PName):
            
         self.__prodName=PName;
          
    def getProdPrice(self):
            
        return self.__prodPrice;
        
    def setProdPrice(self,pPrice):
            
        self.__prodPrice=pPrice;    
        


class Biller:

    
    def __init__(self):
        
        self.__billerId=None;
        self.__billerName=None;
     #   self.__prodPrice=None;
        
    def getBillerId(self):
        
        return self.__billerId;
    
    def setBillerId(self, bId):
        
        self.__billerId=bId;
        
    def getBillerName(self):
            
        return self.__billerName;
        
    def setBillerName(self,bName):
            
         self.__billerName=bName;
          
    def generateBill(self):
        
        print(c.getCustId());
        print(c.getCustName());
        print(c.getCustContact());
        
        print(p.getProdId())
        print(p.getProdName())
        
        print(b.getBillerId())
        print(b.getBillerName())


c=Customer();
c.setCustId(101)
c.setCustName("Rahul")  
c.setCustContact(6299949208)  

p=Product()
p.setProdId(1001)
p.setProdName("Toothbrush")
p.setProdPrice(5000)

b=Biller()
b.setBillerId(501)
b.setBillerName("john")

b.generateBill();
        
        