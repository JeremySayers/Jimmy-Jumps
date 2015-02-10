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
        player_sprite_group_render = pygame.sprite.Group()
        for player in player_sprite_group:
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
            
        return player_sprite_group_render
        
        
    def update_platforms(self, platform_list, player_sprite_group):
        platform_list_render = pygame.sprite.Group()
        for player in player_sprite_group:    
            for platform in platform_list:
                print platform.rect.centery
                platform_render = Platform(platform.rect.width, platform.rect.height, platform.rect.x, platform.rect.y)
                platform_list_render.add(platform_render)
                if (platform.rect.left > player.rect.centerx - self.screen_width/2) and (platform.rect.right < player.rect.centerx + self.screen_width/2):
                    if (platform.rect.bottom > player.rect.centery - self.screen_height/2) and (platform.rect.top < player.rect.centery + self.screen_height/2):
                        if platform.rect.centerx < player.rect.centerx:
                            platform_render.rect.centerx = player.rect.centerx - platform.rect.centerx
                        elif platform.rect.centerx > player.rect.centerx:
                            platform_render.rect.centerx = (platform.rect.centerx - player.rect.centerx) + player.rect.centerx
                        
                        if platform.rect.centery < player.rect.centery:
                            platform_render.rect.centery = player.rect.centery - platform.rect.centery
                        elif platform.rect.centery > player.rect.centery:
                            platform_render.rect.centery = (platform.rect.centery - player.rect.centery) + player.rect.centery
            
        return platform_list_render
                        
                        
                        
                        
        
        