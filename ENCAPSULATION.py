# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:18:24 2024

@author: Rahul Kumar
"""

class Employee:
    
    def __init__(self):
        
        self.__empId=None;
        self.__empName=None;
        self.__empSal=None;
        
    def getEmpId(self):
        
        return self.__empId;
    
    def setEmpId(self, empId):
        
        self.__empId=empId;
        
    def getEmpName(self):
            
        return self.__empName;
        
    def setEmpName(self,empName):
            
         self.__empName=empName;
          
    def getEmpSal(self):
            
        return self.__empSal;
        
    def setEmpSal(self,empSal):
            
        self.__empSal=empSal;
        
e1=Employee()
e1.setEmpId(101)
e1.setEmpName("John")
e1.setEmpSal(5000)
print("*************EMP1 data**********")
print(e1.getEmpId())
print(e1.getEmpName())
print(e1.getEmpSal())


e2=Employee()
e2.setEmpId(102)
e2.setEmpName("Jacob")
e2.setEmpSal(4000)
print("*************EMP2 data**********")
print(e2.getEmpId())
print(e2.getEmpName())
print(e2.getEmpSal())
            
e3=Employee()
e3.setEmpId(103)
e3.setEmpName("David")
e3.setEmpSal(6000)
print("*************EMP3 data**********")
print(e3.getEmpId())
print(e3.getEmpName())
print(e3.getEmpSal())
                        
            
                  
            
        
    
        
        