'''
Created on Feb 5, 2015

@author: Jeremy
'''
import pygame


class Player(pygame.sprite.Sprite):
    '''
    Local Variables for movement, and jumping
    '''
    is_moving_left = False
    is_moving_right = False
    player_mid_jump = False
    player_wall_jump = False
    player_x_speed = 5
    
    '''
    Creates the player object, setting basic properties
    and it's image.
    '''
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
        self.rect.y = 0
        self.rect.x = 20

    '''
    Where most of the magic happens, more comments to come
    '''
    def update(self, platform_list):
        self.platform_list = platform_list
        self.calc_gravity()
        
        '''
        The first block is to see if the player should be moving, and if it should,
        make sure that it's with in the screens bounds (Or maps in the future ^_^)
        '''
        if self.is_moving_left and self.rect.x > 0:
            self.rect.x -= self.player_x_speed
        elif self.is_moving_right and self.rect.x < self.screen_width - self.width:
            self.rect.x += self.player_x_speed
        
        '''
        This next block checks to see if there is a platform colliding with the player
        in terms of moving horizontally, and if so, places the player at the corresponding side of it
        '''
        platform_hit = pygame.sprite.spritecollideany(self, self.platform_list)
        if platform_hit != None:
            if self.is_moving_right:
                self.rect.right = platform_hit.rect.left
            elif self.is_moving_left:
                self.rect.left = platform_hit.rect.right
        
        '''
        Now we move the player vertically and then check to make sure we didn't collide with anything.
        If we did, we just set the object to be above or below what it collided with depending on its'
        y velocity
        '''
        self.rect.y += self.y_vel

        platform_hit = pygame.sprite.spritecollideany(self, self.platform_list)
        if platform_hit != None:
            if self.y_vel > 0:
                self.rect.bottom = platform_hit.rect.top
            elif self.y_vel < 0:
                self.rect.top = platform_hit.rect.bottom

            # Stop our vertical movement
            self.y_vel = 0

    def calc_gravity(self):
        '''
        Moves the player's rect down 2 pixels incase we are working with a moveing platform,
        then checks for collisions with platforms
        '''
        self.rect.y += 2
        platform_hit = pygame.sprite.spritecollideany(self, self.platform_list)
        self.rect.y -= 2

        '''
        The first if checks if we are on the ground or possibly 'in' the ground,
        and if so it resets us to the ground height
        '''
        if (self.rect.bottom >= self.screen_height  and self.y_vel >= 0):
            self.y_vel = 0
            self.player_mid_jump = False
            self.player_wall_jump = False
            self.rect.bottom = self.screen_height
        elif (platform_hit and self.y_vel >= 0):
            self.y_vel = 0                                      #The else see's if we are instead hitting a platform from the top. If we are
            self.player_mid_jump = False                        #it stops us and places us on top of the platform
            self.player_wall_jump = False
            self.rect.bottom = platform_hit.rect.top
        else:
            self.y_vel += .35                                   #This last bit just increases our velocity if we arn't hitting anything, I feel like there's a word for it....

    def jump(self):
        '''
        Moves the player's rect down 2 pixels incase we are working with a moveing platform,
        then checks for collisions with platforms
        '''
        self.rect.y += 2
        platform_hit = pygame.sprite.spritecollideany(self, self.platform_list)
        self.rect.y -= 2

        '''
        The first bit checks to see if we are on top of a platform or on the ground.
        If we are then we start our jump! If not it checks to see if we are close enough to a wall
        to perform a wall jump, if we are then once again we jump!
        '''
        if platform_hit or self.rect.bottom >= self.screen_height:
            if self.player_mid_jump == False:
                self.y_vel = -11
                self.player_mid_jump = True
        elif (self.rect.left <= 5 and not self.player_wall_jump) or (self.rect.right >= self.screen_width -5 and not self.player_wall_jump):
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
