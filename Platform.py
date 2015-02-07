'''
Created on Feb 6, 2015

@author: Jeremy
'''

import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        self.image = pygame.Surface([width, height])
        self.image.fill((0,20,240))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    