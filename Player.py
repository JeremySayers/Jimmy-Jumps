'''
Created on Feb 5, 2015

@author: Jeremy
'''
import pygame

class Player(pygame.sprite.Sprite):
    is_moving_left = False
    is_moving_right = False
    player_mid_jump = False
    player_wall_jump = False
    #player_double_jump = False
    player_x_speed = 5
    
    
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self) 
        self.width = 50
        self.height = 50
        self.screen_height = screen_height
        self.screen_width = screen_width
        
        self.x_vel = 0
        self.y_vel = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((155, 255, 20))
        
        self.rect = self.image.get_rect()
        self.rect.y = screen_height
        self.rect.x = 20
        
    def update(self, platform_list):
        self.platform_list = platform_list
        self.calc_gravity()
        
        if self.is_moving_left and self.rect.x > 0:
            self.rect.x -= self.player_x_speed
        elif self.is_moving_right and self.rect.x < self.screen_width - self.width:
            self.rect.x += self.player_x_speed
        
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.is_moving_right:
                self.rect.x = block.rect.x - self.rect.width
            elif self.is_moving_left:
                # Otherwise if we are moving left, do the opposite.
                self.rect.x = block.rect.x + block.rect.width
        
        self.rect.y += self.y_vel
        
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            if self.y_vel > 0:
                self.rect.y = block.rect.y - self.rect.height
            elif self.y_vel < 0:
                self.rect.y = block.rect.y + block.rect.height
    
            # Stop our vertical movement
            self.y_vel = 0
        
    def calc_gravity(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        self.rect.y -= 2
        
        # See if we are on the ground.
        if (self.rect.y >= self.screen_height - self.rect.height  and self.y_vel >= 0):
            self.y_vel = 0
            self.player_mid_jump = False
            self.player_wall_jump = False
            #self.player_double_jump = False
            self.rect.y = self.screen_height - self.rect.height
        elif (len(platform_hit_list) > 0 and self.y_vel >= 0):
            self.y_vel = 0
            self.player_mid_jump = False
            self.player_wall_jump = False
            self.rect.y = platform_hit_list[0].rect.y - self.rect.height
        else: 
            self.y_vel += .35
    
    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= self.screen_height:
            if self.player_mid_jump == False:
                self.y_vel = -11
                self.player_mid_jump = True
        elif (self.rect.x <= 5 and not self.player_wall_jump and self.is_moving_left) or (self.rect.x > self.screen_width - self.width -5 and not self.player_wall_jump and self.is_moving_right):
            self.y_vel = -11
            self.player_mid_jump = True
            self.player_wall_jump = True
    
    def go_right(self):
        self.is_moving_left = False
        self.is_moving_right = True
        
    def go_left(self):
        self.is_moving_left = True
        self.is_moving_right = False
        
    def stop_right(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        self.is_moving_right = False
        
    def stop_left(self):
        self.is_moving_left = False
    
        