# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 06:03:48 2024

@author: Rahul Kumar
"""

class Employee:
    
    def display_details(self):
        print("Employee id is",self.empID);
        print("Employee name is ", self.empName);
        print("Employee department is", self.empDep);
        
    def __init__(self,empID,empName,empDep):
        self.empID=empID;
        self.empName=empName;
        self.empDep=empDep;
        
e1=Employee(1, "Rahul" ,10)
e1.display_details();

e2=Employee(2, "rishi",20)
e2.display_details();        

e3=Employee(3,"sagar",30)
e3.display_details()