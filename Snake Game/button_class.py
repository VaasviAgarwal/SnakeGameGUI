import pygame
from settings import *

class Button:
    def __init__(self, game, x, y, width, height, bg_color,  hover_color=None, function = None, text=None):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.hovered = False
        self.function = function
        self.text = text
        self.font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', 24)

    def update(self):
        cursor = pygame.mouse.get_pos()
        if self.x+self.width > cursor[0] >self.x and self.y+self.height > cursor[1] > self.y:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if not self.hovered:
            pygame.draw.rect(self.game.screen, self.bg_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.game.screen, self.hover_color, (self.x, self.y, self.width, self.height))       
        pygame.draw.rect(self.game.screen, (255, 255, 255), (self.x, self.y, self.width, 2))
        pygame.draw.rect(self.game.screen, (255, 255, 255), (self.x, self.y, 2, self.height))
        pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x, self.y+self.height-1, self.width+2, 3))
        pygame.draw.rect(self.game.screen, (0,0,0), (self.x + self.width-1, self.y, 3, self.height+2))
        self.show_text()
    
    def click(self):
        if self.function != None:
            self.function()
        else:
            pass

    def show_text(self):
        if self.text != None:
            text = self.font.render(self.text, True, BUTTON_TEXT_COLOR)
            text_size = text.get_size()
            text_x = self.x+(self.width/2) - (text_size[0]/2)
            text_y = self.y + (self.height/2) - (text_size[1]/2)
            self.game.screen.blit(text, (text_x, text_y))



