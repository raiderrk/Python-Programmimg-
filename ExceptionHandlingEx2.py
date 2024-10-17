# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:16:02 2024

@author: Rahul Kumar
"""

class InvalidAgeError(BaseException):
    
    def __init__(self):
        message="Enter the valid age"
        
        print(message);
        
class Vote:
    
    def CheckAge(self,age):
        
        self.age=age;
        if age>=18:
            print("your eligible for voting")
            
        else:
            
            raise InvalidAgeError();
            
        
            
v=Vote() 
try:
    
    
   v.CheckAge(17)    

except InvalidAgeError:

   pass     
    
        
        