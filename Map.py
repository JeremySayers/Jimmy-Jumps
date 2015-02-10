'''
Created on Feb 7, 2015

@author: Jeremy
'''

import pygame

class Map(object):
    
    platform_list = None
    background = None
    def __init__(self):
        self.platform_list = pygame.sprite.Group()
        
    def update(self):
        self.platform_list.update()
        
    def draw(self, screen):
        self.platform_list.draw(screen)
        
