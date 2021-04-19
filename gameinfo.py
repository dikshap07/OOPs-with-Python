# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:27:40 2021

@author: Dikhsha
"""

class GameInfo():
    
    author = 'Diksha'
    
    
    
    def __init__(self,game_title):
        
        self.title = game_title
        
    def welcome(self):
        
        print('Welcome to ',self.title)
 
    @staticmethod
    
    def info():
        
        print('Made using the OOP RPG creator')
        
    @classmethod
    
    def credits(cls):
        
        print("Thankyou for playing!")
        
        print('Created by: ', cls.author)
        
        