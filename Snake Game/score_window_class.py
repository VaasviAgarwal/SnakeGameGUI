import pygame
from settings import *

pygame.init()
class Score_Window:
    def __init__(self, game):
        self.game = game
        self.pos = OFFSET
        self.width = 15*40
        self.height = 15*40
        self.rows = 15
        self.cols = 15
        self.first = pygame.image.load('Graphics/first.png').convert_alpha()
        self.second = pygame.image.load('Graphics/second.png').convert_alpha()
        self.third = pygame.image.load('Graphics/third.png').convert_alpha()
        self.fourth = pygame.image.load('Graphics/fourth.png').convert_alpha()
        self.fifth = pygame.image.load('Graphics/fifth.png').convert_alpha()
        self.si = pygame.image.load('Graphics/snake.png').convert_alpha()

    def draw(self):
        self.draw_window()
        self.draw_table()

    def draw_window(self):
        pygame.draw.rect(self.game.screen, WHITE, (30, 150, self.width, self.height-30))
        pygame.draw.rect(self.game.screen, (0, 185, 185), (0, 0, SCREEN_W, 120))
        si_r = pygame.Rect(420, 470, 198, 254)
        self.game.screen.blit(self.si, si_r)
    
    def draw_table(self):

        self.game.show_text('RANK', [120, 235], 78)
        self.game.show_text('SCORE', [262, 235], 78)
        x = 150
        for i in range(1, 8):
            y = i*70
            if i <=2 or i == 7:
                t = 3
            else :
                t = 1
            pygame.draw.rect(self.game.screen, BLACK, (75, y + x, 300, t))
        pygame.draw.rect(self.game.screen, BLACK, (75, 220, 3, 420))
        pygame.draw.rect(self.game.screen, BLACK, (375, 220, 3, 423))
        pygame.draw.rect(self.game.screen, BLACK, (225, 220, 3, 423))

        first_rect = pygame.Rect(132, 297, 60,60)
        self.game.screen.blit(self.first, first_rect)

        second_rect = pygame.Rect(132, 367, 60,60)
        self.game.screen.blit(self.second, second_rect)

        third_rect = pygame.Rect(132, 437, 60,60)
        self.game.screen.blit(self.third, third_rect)

        fourth_rect = pygame.Rect(132, 507, 60,60)
        self.game.screen.blit(self.fourth, fourth_rect)

        fifth_rect = pygame.Rect(132, 577, 60,60)
        self.game.screen.blit(self.fifth, fifth_rect)

