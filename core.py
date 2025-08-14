import pygame

# This file holds a bunch of supporting architecture for our game. It is 
# basically the lowest level of our code.

# This should not import anything other than pygame!

class Inputs:
    def __init__(self):
        self.keys = {}
        self.mouse_pos = pygame.Vector2()
        self.mouse_buttons = (0,0,0)
        
    def press(self, key:int):
        self.keys[key] = True
    
    def unpress(self, key:int):
        self.keys[key] = False
        
    def update(self):
        self.mouse_buttons = pygame.mouse.get_pressed(3)
        self.mouse_pos.update(pygame.mouse.get_pos())
        
    def get_key(self, key:int) -> bool:
        if key in self.keys:
            return self.keys[key]
        else:
            return False
        
class SpriteSheet:
    def __init__(self, filepath:str, image_size:tuple[int,int]):
        self.sheet = pygame.image.load(filepath)
        num_images = self.sheet.get_width() // image_size[0]
        self.images = [self.sheet.subsurface(pygame.Rect(x * image_size[0], 0, image_size[0], image_size[1])) for x in range(0, num_images)]

    def get_image(self, index:int) -> pygame.Surface:
        return self.images[index]