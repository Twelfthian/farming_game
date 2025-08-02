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
        ...