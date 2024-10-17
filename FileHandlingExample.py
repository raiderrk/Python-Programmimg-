# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:46:22 2024

@author: Rahul Kumar
"""

file=open("Rahul.text",'w');
file.write("jspider")
file.close();


file=open("Rahul.text",'r');
print(file.read())
file.close();



file=open("Rahul.text",'a');
file.write("basvangudi")

file.close();

