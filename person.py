# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:32:45 2024

@author: Rahul Kumar
"""

class Person:
    
    def info(self, name,email):
        
        self.name=name;
        self.email=email;
        
        return email,name
      # print(name,email)
        
    def travel(self):
        print("travelling");
        
        
class Student(Person):
     
    def sinfo(self, studenId):
        
       self.studenId=studenId;
    #   print(  self.studenId )
       
       
p=Person()
p.info("rahul", "rahul@gmail.com")
print(p.info())
s=Student()
s.sinfo(100)
#Student.sinfo()
s.travel()      
          
          
          

              
    