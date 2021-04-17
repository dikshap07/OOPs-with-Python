# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:26:34 2021

@author: Diksha
"""
class Room():
    
    def __init__(self,room_name):
        
        self.name = room_name
        self.linked_rooms = {}
        self.description = None

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
        
            
    