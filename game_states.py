import pygame
from core import *
from game_data import GAME_DATA
from player import Player
from tile import Tile

from debugging import debug_print

class StateHandler:
    '''This is the object that will hold and handle the `GameStates`. It is a `Singleton`.'''
    _instance = None
    _initialized = False

    def __new__(cls) -> "StateHandler":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized: return
        self._initialized = True

        self.states:"list[GameState]" = []

    def update(self, inputs:Inputs, dt:float):
        assert len(self.states) > 0
        self.states[-1].update(inputs, dt)

    def draw(self, display:pygame.Surface):
        self.states[-1].draw(display)

class GameState:
    '''This is the generic `GameState` class. For each new `GameState`, the methods and attributes in here
    should also exist in each of the subclasses (but not `enter_state` and `destroy_state`). Make sure that
    `super().__init__( <args>, <kwargs> )` is used in the `__init__` function and that each new `GameState`
    inherits from this generic class.'''
    def __init__(self):
        ...

    def update(self, inputs:Inputs, dt:float):
        '''Standard `update` method for `GameState`. Each new `GameState` must have this method and must
        accept the same arguments.'''
        ...

    def draw(self, display:pygame.Surface):
        '''Standard `draw` method for `GameState`. Each new `GameState` must have this method and must
        accept the same arguments.'''
        ...

    def enter_state(self):
        '''Makes this `GameState` the current state in the `StateHandler`'''
        StateHandler().states.append(self)

    def destroy_state(self):
        '''Removes the `GameState` from the `StateHandler`'''
        StateHandler().states.remove(self)

class WorldState(GameState):
    '''This is the `GameState` where our player will run around and do things in the world.'''
    def __init__(self, world_size:tuple[int,int], player_pos:tuple[int,int]):
        super().__init__()
        self.player = Player(player_pos)
        # tile_holder is just an easy way to access specific tiles, but it also holds the tiles
        self.tile_holder = {(x,y): Tile((x * GAME_DATA["world"]["tile"]["size"][0],
                                         y * GAME_DATA["world"]["tile"]["size"][1]))
                                         for y in range(world_size[1]) for x in range(world_size[0])}
        # tile_group will hold references to all the tiles for sprite reasons
        self.tile_group:pygame.sprite.Group[Tile] = pygame.sprite.Group(*list(self.tile_holder.values()))

    def update(self, inputs:Inputs, dt:float):
        speed_factor = self.player.speed * dt
        self.player.rect.x += (inputs.get_key(pygame.K_d) - inputs.get_key(pygame.K_a)) * speed_factor
        self.player.rect.y += (inputs.get_key(pygame.K_s) - inputs.get_key(pygame.K_w)) * speed_factor

        for tile in self.tile_group:
            tile.update(inputs, dt)

    def draw(self, display:pygame.Surface):
        display.fill((0,0,0)) # color screen black

        for tile in self.tile_group:
            display.blit(tile.image, tile.rect)

        display.blit(self.player.image, self.player.rect)