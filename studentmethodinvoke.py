# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:30:20 2024

@author: Rahul Kumar
"""

class Student:
    
    def CollectMarkSheet(self,rollId ,perc):
        print("Parcentage of the student with rollnumber",rollId,"is" , perc);
       
s1=Student();
s1.CollectMarkSheet(101,78);
print(s1)

s2=Student();
s2.CollectMarkSheet(102,66);
print(s2)

s3=Student();
s3.CollectMarkSheet(103, 88);
print(s3)
        



        
        