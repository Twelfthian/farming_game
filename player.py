import pygame
from game_data import GAME_DATA

class Player(pygame.sprite.Sprite):
    def __init__(self, pos:tuple[int,int]):
        super().__init__()
        self.image = pygame.Surface((25,25))
        self.rect = self.image.get_frect(center = pos)
        self.speed = GAME_DATA["player"]["speed"]

        self.image.fill((255,0,0))