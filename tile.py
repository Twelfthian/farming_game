import pygame
from core import *
from game_data import GAME_DATA
import assets

class Tile(pygame.sprite.Sprite):
    def __init__(self, world_pos:tuple[int,int]):
        super().__init__()
        self.rect = pygame.Rect(*world_pos, GAME_DATA["world"]["tile"]["size"][0],
                                GAME_DATA["world"]["tile"]["size"][1])
        
        self.state = assets.GRASS # this is an index (just an int)
        self.image = assets.TILE_IMAGES[self.state] # this is an image
        
        # TODO: come up with a better system for all this stuff vv
        self.hovered = False
        self.prev_hovered = False
        self.clicked = False
        self.prev_clicked = False
        
    def update(self, inputs:Inputs, dt:float):
        self.prev_hovered = self.hovered
        self.prev_clicked = self.clicked
        
        if self.rect.collidepoint(*inputs.mouse_pos.xy):
            self.hovered = True
            if inputs.mouse_buttons[0]:
                self.clicked = True
            else:
                self.clicked = False
        else:
            self.hovered = False
            self.clicked = False
        
        if self.clicked and not self.prev_clicked:
            self.state = (self.state + 1) % 3
        elif (self.hovered and not self.prev_hovered) or (self.hovered and self.prev_clicked and not self.clicked):
            ...
        elif self.prev_hovered and not self.hovered:
            ...
            
        self.image = assets.TILE_IMAGES[self.state]