import pygame

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

GRASS = 0
DIRT = 1
TILLED = 2

tile_images = {
    DIRT: pygame.image.load("dirt.jpg"),
    TILLED: pygame.image.load("tilled_dirt.jpg"),
    GRASS: pygame.image.load("grass.jpg"),
    "flowers": pygame.image.load("grass_flowers.jpg"),
}

TILE_SIZE = 64
class Tile(pygame.sprite.Sprite):
    def __init__(self, world_pos:tuple[int,int]):
        self.rect = pygame.Rect(*world_pos, TILE_SIZE, TILE_SIZE)
        self.state = GRASS
        self.image = tile_images[GRASS]
                
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
            
        self.image = tile_images[self.state]

class TileHandler:
    def __init__(self, world_size:tuple[int,int]):
        self.tiles = {(x,y): Tile((x * TILE_SIZE, y * TILE_SIZE)) for y in range(world_size[1]) for x in range(world_size[0])}

    def draw(self, display:pygame.Surface):
        for tile in self.tiles.values():
            display.blit(tile.image, tile.rect)
            
    def update(self, inputs:Inputs, dt:float):
        for tile in self.tiles.values():
            tile.update(inputs, dt)

if __name__ == "__main__":
    SCREEN_SIZE = (800,600)
    
    dirt_images = [pygame.image.load("dirt.jpg"), pygame.image.load("tilled_dirt.jpg")]
    
    pygame.init()
    
    display = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF)
    clock = pygame.Clock()
    inputs = Inputs()
    tile_handler = TileHandler((12,9))
    
    player_rect = pygame.Rect(0,0,10,10)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                inputs.press(event.key)
                
            elif event.type == pygame.KEYUP:
                inputs.unpress(event.key)
        inputs.update()
        
        player_rect.x += (inputs.get_key(pygame.K_d) - inputs.get_key(pygame.K_a)) * 10
        player_rect.y += (inputs.get_key(pygame.K_s) - inputs.get_key(pygame.K_w)) * 10

        tile_handler.update(inputs, 0.0)
        
        display.fill((0,0,0))
                
        tile_handler.draw(display)
        pygame.draw.rect(display, "red", player_rect)
        pygame.display.flip()
        pygame.display.set_caption(f"FPS: {clock.get_fps()}")
        
        clock.tick(60)