import pygame
import random
import copy
from settings import *

pygame.init()

class Food:
    def __init__(self, game):
        self.game = game
        self.game_window = self.game.game_window
        self.origin = copy.deepcopy(self.game_window.pos)
        self.pos = self.set_pos()
        self.FRUIT = pygame.image.load('Graphics/orange.png').convert_alpha()
    
    def set_pos(self):
        set = False
        while True:
            pos = self.update()
            c = 0
            for i in range(0, self.game.snake.length-1):
                if self.game.snake.body[i] == pos:
                    c = 1
            if not c:
                return pos

    def update(self):
        return [random.randint(0, self.game_window.cols-1), random.randint(0, self.game_window.rows -2)]

    def draw(self):
        fruit_rect = pygame.Rect(int((self.pos[0]*CELL_SIZE)+30), int((self.pos[1]*CELL_SIZE)+120), CELL_SIZE, CELL_SIZE)
        self.game.screen.blit(self.FRUIT, fruit_rect)

        