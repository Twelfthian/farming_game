import pygame, os

# This file will only have assets in it

# This should not import anything other than pygame and os!

# TODO: use os module to get paths that work across different os's

GRASS = 0
DIRT = 1
TILLED = 2
FLOWERS = 3

TILE_IMAGES = {
    DIRT: pygame.image.load("assets/dirt.jpg"),
    TILLED: pygame.image.load("assets/tilled_dirt.jpg"),
    GRASS: pygame.image.load("assets/grass.jpg"),
    FLOWERS: pygame.image.load("assets/grass_flowers.jpg"),
}