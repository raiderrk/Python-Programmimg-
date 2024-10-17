# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:44:29 2024

@author: Rahul Kumar
"""

def checkLeapYear(year):
    
    if (year//4*4==year and  year//100*100!=year) or  year//400*400==year:
        
    #if (year//4==year/4 and  year//100!=year/100) or  year//400==year/400:

        return "leap year"
    else:
        return "not leap year"

year=int(input("Enter the value"))
print(checkLeapYear(year))