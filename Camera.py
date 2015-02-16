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
        
    def update_player(self, player):
        player_sprite_group_render = pygame.sprite.Group()
        player_render = Player(self.map_width, self.map_height)
        player_sprite_group_render.add(player_render)
       
        if player.rect.centerx < self.screen_width/2:
            player_render.rect.centerx = player.rect.centerx
        elif player.rect.centerx > self.map_width - (self.screen_width/2):
            player_render.rect.centerx = (self.screen_width/2) + (player.rect.centerx - (self.map_width - (self.screen_width/2)))
        else:
            player_render.rect.centerx = self.screen_width/2
             
             
        if player.rect.centery < self.screen_height/2:
            player_render.rect.centery = player.rect.centery
        elif player.rect.centery > self.map_height - (self.screen_height/2):
            player_render.rect.centery = (self.screen_height/2) + (player.rect.centery - (self.map_height - (self.screen_height/2)))
        else:
            player_render.rect.centery = self.screen_height/2
           
        return (player_sprite_group_render,
                player.rect.centerx - player_render.rect.centerx,
                player.rect.centery - player_render.rect.centery)
       
       
    def update_platforms(self, platform_list, xoff, yoff):
        platform_list_render = pygame.sprite.Group()  
        for platform in platform_list:
            platform_render = Platform(platform.rect.width, platform.rect.height, platform.rect.x - xoff, platform.rect.y - yoff)
            platform_list_render.add(platform_render)
           
        return platform_list_render
                        
                        
                        
                        
        
        