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
        player_sprite_group_render = player_sprite_group.copy()
        for player in player_sprite_group_render:
            
            if player.rect.centerx < self.screen_width/2:
                player.rect.centerx = player.rect.centerx
            elif player.rect.centerx > self.map_width - (self.screen_width/2):
                player.rect.centerx = (self.screen_width/2) + (player.rect.centerx - (self.map_width - (self.screen_width/2)))
            else:
                player.centerx = self.screen_width/2
                
                
            if player.rect.centery < self.screen_height/2:
                player.rect.centery = player.rect.centery
            elif player.rect.centery > self.map_height - (self.screen_height/2):
                player.rect.centery = (self.screen_height/2) + (player.rect.centery - (self.map_height - (self.screen_height/2)))
            else:
                player.centery = self.screen_height/2
            
        return player_sprite_group_render
        
        
    def update_platforms(self, platform_list, player):
        platform_list = platform_list.copy()
            
        for platform in platform_list:
            if (platform.rect.left > player.rect.centerx - self.screen_width/2) and (platform.rect.right < player.rect.centerx + self.screen_width/2):
                if (platform.rect.bottom > player.rect.centery - self.screen_height/2) and (platform.rect.top < player.rect.centery + self.screen_height/2):
                    if platform.rect.centerx < player.rect.centerx:
                        platform.rect.centerx = player.rect.centerx - platform.rect.centerx
                    elif platform.rect.centerx > player.rect.centerx:
                        platform.rect.centerx = (platform.rect.centerx - player.rect.centerx) + player.rect.centerx
                    
                    if platform.rect.centery < player.rect.centery:
                        platform.rect.centery = player.rect.centery - platform.rect.centery
                    elif platform.rect.centery > player.rect.centery:
                        platform.rect.centery = (platform.rect.centery - player.rect.centery) + player.rect.centery
        
        return platform_list
                        
                        
                        
                        
        
        