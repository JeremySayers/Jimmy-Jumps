'''
Created on Feb 4, 2015

@author: Jeremy
'''

import pygame
import sys
from Player import Player
from Platform import Platform

FPS = 120
RESOLUTION = (800, 600)
FULLSCREEN = False
DOUBLEBUFFER = False

class Game(object):
    def __init__(self, screen):
        self.player = Player(800, 600)
        self.active_sprite_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.active_sprite_list.add(self.player)
        self.platform_list.add(Platform(200, 30, 270, 220))
        self.platform_list.add(Platform(200, 30, 300, 420))
        self.platform_list.add(Platform(200, 30, 600, 110))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 30)
        self.game_loop()
        
            
    def game_loop(self):
        while True:
            self.dt = self.clock.tick(FPS)
            self.update()
            self.process_events()
            self.draw_screen()
    
    def update(self):
        self.active_sprite_list.update(self.platform_list)   
             
    def draw_screen(self):
        screen.fill((0, 0, 0))
        self.active_sprite_list.draw(screen)
        self.platform_list.draw(screen)
        self.display_fps()
        pygame.display.flip()
                        
    def process_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    if event.key == pygame.K_l:
                        if screen.get_flags() & FULLSCREEN:
                            pygame.display.set_mode(RESOLUTION)
                        else:
                            pygame.display.set_mode(RESOLUTION, FULLSCREEN)
                
                    elif event.key == pygame.K_a:
                        self.player.go_left()
                    elif event.key == pygame.K_d:
                        self.player.go_right()
                    elif event.key == pygame.K_SPACE:
                        self.player.jump()
 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.stop_left()
                    if event.key == pygame.K_d:
                        self.player.stop_right()
                        
    def display_fps(self):
        framerate_text = self.font.render("FPS: " + str(self.clock.get_fps()) , 1, (255,255,255))
        screen.blit(framerate_text, (10, 10))

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Jimmy")
    screen = pygame.display.set_mode(RESOLUTION, (pygame.FULLSCREEN if FULLSCREEN else 0) | (pygame.DOUBLEBUF if DOUBLEBUFFER else 0))
    Game(screen)