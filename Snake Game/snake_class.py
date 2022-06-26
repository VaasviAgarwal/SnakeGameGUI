import pygame
import random
import copy
from settings import *
from food_class import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

class Snake:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.game_window = game.game_window
        self.origin = copy.deepcopy(self.game_window.pos)
        self.direction = [0,0]
        self.body = [[5,7], [4,7]]
        self.pos = self.body[0]
        self.length = 2
        self.head_up = pygame.image.load('Graphics/headup.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/headdown.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/headright.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/headleft.png').convert_alpha()
        self.tail_up = pygame.image.load('Graphics/tailup.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/taildown.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tailright.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tailleft.png').convert_alpha()
        self.body_vertical = pygame.image.load('Graphics/bodyvertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/bodyhorizontal.png').convert_alpha()
        self.body_tr = pygame.image.load('Graphics/tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
        self.crash_sound = pygame.mixer.Sound('Sound/crash.wav')

    def update(self):
        if self.length-2 >=0 and self.length -2 < 10:
            level = 2
        elif self.length-2<= 30:
            level = 3   
        elif self.length-2<= 55:
            level = 6
        elif self.length - 2<= 80:
            level = 8
        else:
            level = 10
        if self.game.frame_count%(FPS//level) == 0:
            self.pos[0]+=self.direction[0]
            self.pos[1]+=self.direction[1]
            if self.pos[0]<0 or self.pos[0]>self.game_window.cols-1:
                self.die()
            if self.pos[1]<0 or self.pos[1]>self.game_window.rows-1:
                self.die()
            if self.pos[0]== self.game.food.pos[0] and self.pos[1] == self.game.food.pos[1]:
                self.eat()
            self.set_body()
            if self.hit_self():
                self.die()

    def draw(self):
        if self.direction == [0,0]:
            br = pygame.Rect(230, 400, 40, 40)
            self.game.screen.blit(self.head_right, br)
            br = pygame.Rect(190, 400, 40, 40)
            self.game.screen.blit(self.tail_right, br)
        else:
            for index, block in enumerate(self.body):
                x_pos = (block[0]*CELL_SIZE) + 30
                y_pos = (block[1]*CELL_SIZE) + 120
                block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                if index == 0:
                    h = self.body[0]
                    h1 = self.body[1]
                    hx = h1[0] - h[0]
                    hy = h1[1] - h[1]
                    hr = [hx, hy]
                    if hr == [1,0]:
                        self.game.screen.blit(self.head_left, block_rect)
                    elif hr ==[-1,0]:
                        self.game.screen.blit(self.head_right, block_rect)
                    elif hr == [0,1]:
                        self.game.screen.blit(self.head_up, block_rect)
                    elif hr == [0,-1]:
                        self.game.screen.blit(self.head_down, block_rect)  
                elif index == len(self.body)-1:
                    h = self.body[-2]
                    h1 = self.body[-1]
                    hx = h1[0] - h[0]
                    hy = h1[1] - h[1]
                    hr = [hx, hy]
                    if hr == [1,0]:
                        self.game.screen.blit(self.tail_left, block_rect)
                    elif hr == [-1,0]:
                        self.game.screen.blit(self.tail_right, block_rect)
                    elif hr == [0,1]:
                        self.game.screen.blit(self.tail_up, block_rect)
                    elif hr == [0,-1]:
                        self.game.screen.blit(self.tail_down, block_rect)      
                else:
                    p = self.body[index+1]
                    n = self.body[index-1]
                    px = p[0] - block[0]
                    py = p[1] - block[1]
                    nx = n[0] - block[0]
                    ny = n[1] - block[1]
                    if px == nx:
                        self.game.screen.blit(self.body_vertical, block_rect)

                    elif py == ny:
                        self.game.screen.blit(self.body_horizontal, block_rect)    
                    else:
                        if px == -1 and ny == -1 or py == -1 and nx == -1:
                            self.game.screen.blit(self.body_tl, block_rect)
                        if px == -1 and ny == 1 or py == 1 and nx == -1:
                            self.game.screen.blit(self.body_bl, block_rect)
                        if px == 1 and ny == -1 or py == -1 and nx == 1:
                            self.game.screen.blit(self.body_tr, block_rect)
                        if px == 1 and ny == 1 or py == 1 and nx == 1:
                            self.game.screen.blit(self.body_br, block_rect)
   
    def hit_self(self):
        if self.length>2:
            for idx, pos in enumerate(self.body):
                if self.pos == pos and idx !=0 :
                    return True
        return False
            
    def set_body(self):
        x,y = self.pos[0], self.pos[1]
        self.body.insert(0, [x,y])
        self.body = self.body[:self.length]

    def eat(self):
        self.length +=1
        self.game.food = Food(self.game)
        self.crunch_sound.play()

    def die(self):
        self.crash_sound.play()
        self.crash_sound.play()
        self.game.state = 'dead'
        self.game.active_buttons = self.game.dead_buttons
        self.game.check_scores()


