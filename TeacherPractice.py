# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:40:34 2024

@author: Rahul Kumar
"""

class Teacher:
    
    def details(self,Name,Age):
        self.name=Name;
        self.age=Age;
        print(self.name,self.age);
        
    @classmethod 
    def teches(cls,self):
        
        a=Teacher();
        a.b=("Teacher Teches students");
        print(a.b);
        print(self)
        
    @staticmethod 
    def work(self,cls):
        
        a1=Teacher();
        a1.b=("teacher assign work to student");
        print(a1.b);
        print(self,cls);
        
t=Teacher();
t.details("rahul", 34);
t.teches(4)
t.work(1,2)  
#Teacher.work()     
        
     