'''
Created on Feb 7, 2015

@author: Jeremy
'''
import pygame
from Map import Map
from Platform import Platform


class Map_01(Map):
    def __init__(self):
        Map.__init__(self)
        
        ''' Locations and sizes of platforms (width, height, x y) ''' 
        map = [[200, 30, 270, 220],
               [200, 30, 300, 420],
               [200, 30, 600, 110]]
        
        for platform in map:
            block = Platform(platform[0], platform[1], platform[2], platform[3])
            self.platform_list.add(block)
        