# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:48:37 2021

@author: Dikhsha
"""

class Item():
    
    def __init__(self,name):
        
        self.name = name
        self.description = None
        

    def set_name(self,item_name):
        
        self.name = item_name
        
    def get_name(self):
        
        return self.name
    
    def set_description(self,description):
        
        self.description = description
        
    def get_description(self):
        
        return self.description
    
    
    #room where item is present in
    
    def set_item_location(self,room_name):
        
        self.location = room_name
        
        
    def get_item_location(self):
        
        return self.location
        
        
        
        