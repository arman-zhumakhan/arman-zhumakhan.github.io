import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its stating position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Store a  decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        
        if self.moving_up and self.rect.top>0:
            self.centery -= self.ai_settings.ship_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            
        # Update the rect object
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    
    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom