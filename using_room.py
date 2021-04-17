# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:30:09 2021

@author: Dikhsha
"""

from room import Room
from character import Enemy
from item import Item



#print(kitchen.name)

#Setting up rooms for the game
kitchen = Room('Kitchen')
ballroom = Room('ballroom')
dining_room = Room('dining_room')
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")
dining_room.set_description("A large room with ornate golden decorations on each wall")
kitchen.set_description("A dank and dirty room buzzing with flies")


#print(ballroom.get_description())


#print(dining_room.get_name())

kitchen.set_name('kitchen')

#print(kitchen.get_name())

kitchen.link_room(dining_room,'south')
dining_room.link_room(ballroom, 'west')
ballroom.link_room(dining_room,'east')
dining_room.link_room(kitchen,'north')
ballroom.link_room(kitchen,'northeast')
kitchen.link_room(ballroom,'southwest')

#print(ballroom.linked_rooms)

#dining_room.get_details()

#moving players form on room to another

 
    
'''current_room = dining_room
while True:
    
    print('\n')
    current_room.get_details()
    command = input('  > ')
    
    current_room = current_room.move(command)'''



#setting up enemy
dave = Enemy('Dave', 'A smelly zombie!!')

#dave.describe()
dave.set_conversation('urrghhhh....murrhrhh..guuhhh..')

dave.set_weakness('Hot iron')

#setting up enemy in a room    

dining_room.set_character(dave)


current_room = dining_room

while current_room is not None:
    
    print('\n')
    
    inhabitant = current_room.get_character()
    print("You are in :")
    current_room.get_details()
    print('\n')
    
    if inhabitant == None:
        print('\n')
        print('No enemy in the room')
        
        command = input(' Which direction to go next:  ')
        
        current_room = current_room.move(command.lower())
        
    else:
        inhabitant.describe()
        print('\n')
        
        command = input(' What do you want to do: ')
    
        if command.lower() in ['north','south','east','west','northeast','southwest']:
                print('\n')
                current_room = current_room.move(command.lower())
        
        elif command.lower() == 'talk':
                print('\n')
                inhabitant.talk()
        
        elif command.lower() == 'fight':
                print('\n')
                weapon = input('Choose your weapon: ')
                print('\n')
                inhabitant.fight(weapon)

        else:
            break
        

#diksha = Item('diksha')

#diksha.set_description('cute sweet girl')

#diksha.set_item_location('kitchen')

#print(diksha.get_description())

#print(diksha.get_item_location())
    
    
