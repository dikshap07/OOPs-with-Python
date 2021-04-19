# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:26:34 2021

@author: Diksha
"""
class Room():
    
    no_of_rooms = 0
    
    def __init__(self,room_name):
        
        self.name = room_name
        self.linked_rooms = {}
        self.description = None
        self.character = None
        self.item = None
        
        Room.no_of_rooms += 1 

    def set_description(self,room_description):
        
        self.description = room_description
        
            
    def get_description(self):
        
        return self.description
    
    def describe(self):
        
        print(self.get_description())
    
    def set_name(self,room_name):
        
        self.name = room_name
    
    def get_name(self):
        
        return self.name
    
    def set_character(self, character_name):
        
        self.character = character_name
        
    def get_character(self):
        
        return self.character
    
    def set_item(self,item_name):
        
        self.item = item_name
    
    def get_item(self):
        
        return self.item
    
    def link_room(self,room_to_link,direction):
        
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked to "+ room_to_link.name + " in "+ direction + ' direction')
    
    
    def get_details(self):
        
        print(self.get_name())
        print(self.description)
        for direction in self.linked_rooms:
            
            room = self.linked_rooms[direction]
            
            print('The '+ room.get_name()+ ' is ' + direction)
            
    def move(self,direction):
        
        if direction in self.linked_rooms:
            
            return self.linked_rooms[direction]
        
        else:
            
            print('you cannot go that way')
            return self
        
            
    
