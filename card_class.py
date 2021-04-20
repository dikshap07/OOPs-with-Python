# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 23:26:30 2021

@author: Dikhsha
"""

class Card():  
    
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        
    
    #string method
    def __str__(self):
        
        return self.rank + ' of ' + self.suit 