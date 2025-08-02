import pygame
from core import *
from game_data import GAME_DATA
from game_states import StateHandler, WorldState

class Game:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(GAME_DATA["display"]["size"], pygame.DOUBLEBUF)
        self.clock = pygame.Clock()
        self.inputs = Inputs()
        self.running = True
        self.inputs = Inputs()

        start_state = WorldState((12,9), (0,0))
        start_state.enter_state()

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                print(f"Game closing.")
                
            elif event.type == pygame.KEYDOWN:
                self.inputs.press(event.key)
                
            elif event.type == pygame.KEYUP:
                self.inputs.unpress(event.key)
        self.inputs.update()

    def run(self):
        dt = 0.0
        while self.running:
            self.event_check()
            
            StateHandler().update(self.inputs, dt)
            StateHandler().draw(self.display)

            pygame.display.flip()
            pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")
            
            dt = self.clock.tick_busy_loop(60) / 1000

if __name__ == "__main__":
    game = Game()
    game.run()