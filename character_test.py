# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:51:38 2021

@author: Dikhsha
"""

from character import Character

nomnom = Character('nomnom','A restaurant manager in SG')
niri = Character('niri', 'A bi developer in SG')
#nomnom.describe()

nomnom.set_conversation('Hi, What can I get you today?')
niri.set_conversation('Hi Can I get some fries')

nomnom.talk()
niri.talk()

niri.fight('Rod')

from character import Enemy

dave = Enemy('Dave', 'Dave is A smelly zombie!!')

dave.describe()

dave.set_conversation('You have some nerve coming here!')

dave.talk()
dave.set_weakness('Hot iron')

#print(dave.get_weakness())

print("[" + nomnom.name + " says]: " + niri.name + ', what will you fight dave with')
weapon = input()

dave.fight(weapon)



