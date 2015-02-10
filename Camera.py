'''
Created on Feb 10, 2015

@author: Jeremy
'''

import pygame
from Player import Player
from Platform import Platform

class Camera(object):
    def __init__(self, screen_width, screen_height, map_width, map_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height
        
    def update_player(self, player_sprite_group):
        self.player_sprite_group = player_sprite_group
        for self.player in self.player_sprite_group:
            
            if self.player.rect.centerx < self.screen_width/2:
                self.player.rect.centerx = self.player.rect.centerx
            elif self.player.rect.centerx > self.map_width - (self.screen_width/2):
                self.player.rect.centerx = (self.screen_width/2) + (self.player.rect.centerx - (self.map_width - (self.screen_width/2)))
            else:
                self.player.centerx = self.screen_width/2
                
                
            if self.player.rect.centery < self.screen_height/2:
                self.player.rect.centery = self.player.rect.centery
            elif self.player.rect.centery > self.map_height - (self.screen_height/2):
                self.player.rect.centery = (self.screen_height/2) + (self.player.rect.centery - (self.map_height - (self.screen_height/2)))
            else:
                self.player.centery = self.screen_height/2
            
        return (self.player_sprite_group)
        
        
    def update_platforms(self, platform_list, player):
        self.player = player
        self.platform_list = platform_list
        self.platform_list_render = platform_list
            
        for platform in self.platform_list:
            if (platform.rect.left > self.player.rect.centerx - self.screen_width/2) and (platform.rect.right < self.player.rect.centerx + self.screen_width/2):
                if (platform.rect.bottom > self.player.rect.centery - self.screen_height/2) and (platform.rect.top < self.player.rect.centery + self.screen_height/2):
                    if platform.rect.centerx < self.player.rect.centerx:
                        platform.rect.centerx = self.player.rect.centerx - platform.rect.centerx
                    elif platform.rect.centerx > self.player.rect.centerx:
                        platform.rect.centerx = (platform.rect.centerx - self.player.rect.centerx) + self.player.rect.centerx
                    
                    if platform.rect.centery < self.player.rect.centery:
                        platform.rect.centery = self.player.rect.centery - platform.rect.centery
                    elif platform.rect.centery > self.player.rect.centery:
                        platform.rect.centery = (platform.rect.centery - self.player.rect.centery) + self.player.rect.centery
        
        return platform_list
                        
                        
                        
                        
        
        