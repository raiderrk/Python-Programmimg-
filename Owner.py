# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:34:50 2024

@author: Rahul Kumar
"""

class Owner:
    
    def callAndRequestMenu(self,chef):
        print("Owner Called chef")
        chef.serveTheMenu();
        self.getGrocieries();
        
    def getGrocieries(self):
        print("chef goes out to get grocieris from shop");
        
class Chef:
     
     def serveTheMenu(self):
         print("chef serve the menu to owner");
         
     def purchaseGrocieries(self):
         print("chef purchase the Grocieries");
                 
     def preparDish(self):
         print("Prepare the Dish");
                     
     def serveToOwner(self):
         print("serve the dish to owner");
c=Chef();        
o=Owner();
o.callAndRequestMenu(c);

c.serveTheMenu()
c.purchaseGrocieries();
c.preparDish()
c.serveToOwner();
        

    
