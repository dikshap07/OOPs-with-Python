# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:50:16 2021

@author: Dikhsha
"""

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    
class Enemy(Character):
    
    
    enemies_defeated = 0
    
    def __init__(self,char_name, char_description):
        
        super().__init__(char_name,char_description)
        self._weakness = None
        
        
    def set_weakness(self, weakness):
        
        self.weakness = weakness

    def get_weakness(self):
        
        return self.weakness
    
    #replacing getter, setter methods for weakness with property
    
    '''@property
    
    def weakness(self):
        
        return self._weakness
    
    @weakness.setter
    
    def weakness(self,weakness):
        
        if weakness.type == 'str':
            
            self._weakness = weakness
        
        else:
            
            print('Invalid weakness')'''
            
    
    
    def set_bribe(self,bribe):
        
        self.bribe = bribe
        
    def get_bribe(self):
        
        return self.bribe
    
    
    def fight(self,combat_item):
        
        if combat_item == self.weakness:
            
            print('You fend ' + self.name + ' off with the '+ combat_item + ' YOU WIN THIS ROUND!!!' )
            Enemy.enemies_defeated += 1
            return True
            
        else:
            
            print(self.name + " crushes you, puny adventurer, YOU LOOSE :( ")
            return False
        
        
    def bribe(self,bribe_item):
        
        if bribe_item == self.bribe:
            
            print(self.name + ' will allow you to go another room for this bribe.')
            return True
            
        else:
            
            print(self.name + ' will not take this bribe')
            
            
class Friend(Character):
    
    def __init__(self, char_name, char_description):
        
        super().__init__(char_name,char_description)
                
        
    def hug(self):
        
        print('You can hug' + self.name)
        
    
        
    
        
        
        

        