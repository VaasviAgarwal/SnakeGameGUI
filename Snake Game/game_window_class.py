import pygame
from settings import *
class Game_Window:
    def __init__(self, game):
        self.game = game
        self.pos = OFFSET
        self.width = 15*40
        self.height = 15*40
        self.rows = 15
        self.cols = 15
    def update(self):
        self.game.snake.update()
    def draw(self):
        self.draw_game_window()
        self.game.snake.draw()
        self.game.food.draw()
    def draw_game_window(self):
        pygame.draw.rect(self.game.screen, WHITE, (self.pos[0], self.pos[1], self.width, self.height))
        pygame.draw.rect(self.game.screen, (0, 185, 185), (0, 0, SCREEN_W, 90))
        grass_color = (159, 236, 238)
        for row in range(15):
            if row%2==0:
                for col in range(15):
                    if col%2==0:
                        grass_rect = pygame.Rect((col*CELL_SIZE)+self.pos[0], (row*CELL_SIZE)+self.pos[1], CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.game.screen, grass_color, grass_rect)
            else:
                for col in range(15):
                    if col%2!=0:
                        grass_rect = pygame.Rect((col*CELL_SIZE)+self.pos[0], (row*CELL_SIZE)+self.pos[1], CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.game.screen, grass_color, grass_rect)  
        pygame.draw.rect(self.game.screen, (255, 255, 255), (30, 120, 2, 600))
        pygame.draw.rect(self.game.screen, (255, 255, 255), (630, 120, 2, 600))
        pygame.draw.rect(self.game.screen, (255, 255, 255), (30, 120, 600, 2))
        pygame.draw.rect(self.game.screen, (255, 255, 255), (30, 720, 600, 2))
