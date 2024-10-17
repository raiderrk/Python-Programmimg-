# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:08:52 2024

@author: Rahul Kumar
"""

class sample:
    def __init__(self):
         print("implicit:-----",self)#implicit /inbuilt ref variable
         pass
rahul=sample();    #user defined ref variable
print("user_defined:-----",rahul)    