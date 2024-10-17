# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:37:29 2024

@author: Rahul Kumar
"""

def checkLeapYear(year):
    
   if year%4==0 and year%100!=0:
       print("its a leap year")
   else:
       print("Not a leap year")
    

    
year =int(input("Enter the year"))

print(checkLeapYear(year))    