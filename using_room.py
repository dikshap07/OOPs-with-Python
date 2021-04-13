# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:30:09 2021

@author: Dikhsha
"""

from room import Room

kitchen = Room('Kitchen')

#print(kitchen.name)

ballroom = Room('ballroom')
dining_room = Room('dining_room')
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")
dining_room.set_description("A large room with ornate golden decorations on each wall")
kitchen.set_description("A dank and dirty room buzzing with flies")


#print(ballroom.get_description())


#print(dining_room.get_name())

kitchen.set_name('kitchen')

#print(kitchen.get_name())

kitchen.link_room(dining_room,'South')
dining_room.link_room(ballroom, 'West')
ballroom.link_room(dining_room,'East')
dining_room.link_room(kitchen,'North')
ballroom.link_room(kitchen,'NorthEast')
kitchen.link_room(ballroom,'SouthWest')

#print(ballroom.linked_rooms)

#dining_room.get_details()

#moving players form on room to another

 
    
current_room = dining_room
while True:
    
    print('\n')
    current_room.get_details()
    command = input('  > ')
    
    current_room = current_room.move(command)
