import pygame, sys
from settings import *
from button_class import *
from game_window_class import *
from snake_class import *
from food_class import *
from score_window_class import *

pygame.init()

class Game:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen  = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.running = True
        self.state = 'intro'
        self.intro_buttons = []
        self.playing_buttons = []
        self.dead_buttons = []
        self.scores_buttons = []
        self.active_buttons  = self.intro_buttons
        self.scores = []
        self.make_buttons()
        self.game_window = Game_Window(self)
        self.score_window = Score_Window(self)
        self.snake = Snake(self)
        self.food = Food(self)
        self.get_scores()
        self.frame_count = 0
        self.fruit = pygame.image.load('Graphics/orange.png').convert_alpha()
        self.intro_image = pygame.image.load('Graphics/intro.png').convert_alpha()
        self.si = pygame.image.load('Graphics/snakeb.png').convert_alpha()
        self.go = pygame.image.load('Graphics/gameover.png').convert_alpha()

    def set_scores(self):
        with open(SAVES_FILE, 'w') as file:
            for score in self.scores:
                file.write(str(score)+'\n')

    def new_highscore(self):
        self.scores.append(self.snake.length-2)
        self.scores.sort()
        self.scores.reverse()
        self.scores = self.scores[:5]
        self.set_scores()

    def check_scores(self):
        for score in self.scores:
            if self.snake.length-2>score:
                self.new_highscore()
                return True

    def get_scores(self):
        with open(SAVES_FILE, 'r') as file:
            for line in file:
                self.scores.append(line.strip())
        for idx, score in enumerate(self.scores):
            self.scores[idx] = int(self.scores[idx])
        self.scores.sort()
        self.scores.reverse()
    
    def make_buttons(self):
        intro_play_button = Button(self, 155, 400, 340, 60, (0, 210, 210), hover_color=(49, 218, 46), function = self.reset, text='PLAY')
        self.intro_buttons.append(intro_play_button)
        viewscores = Button(self, 155, 480, 340, 60, (0, 210, 210), hover_color=(255,235,58), function = self.view_scores, text='VIEW HIGH SCORES')
        self.intro_buttons.append(viewscores)
        intro_quit_button = Button(self, 155 , 560, 340, 60, (0, 210, 210), hover_color=(199, 30, 30), function = self.intro_quit, text='QUIT')
        self.intro_buttons.append(intro_quit_button)

        playing_home_button = Button(self, 500, 20, 120, 45, (214, 214, 214), hover_color=(255,235,58), function = self.back_to_intro, text='HOME')
        self.playing_buttons.append(playing_home_button)
        playing_quit_button = Button(self, 360, 20, 120, 45, (214, 214, 214), hover_color=(255,102,102), function = self.reset, text='RESET')
        self.playing_buttons.append(playing_quit_button)

        dead_play_again_button = Button(self, 150, 435, 370, 70, (0, 210, 210), hover_color=(159, 236, 238), function = self.reset, text='PLAY AGAIN')
        self.dead_buttons.append(dead_play_again_button)
        dead_viewscores = Button(self, 150, 535, 370, 70, (0, 210, 210), hover_color=(159, 236, 238), function = self.view_scores, text='VIEW HIGH SCORES')
        self.dead_buttons.append(dead_viewscores)
        dead_quit_button = Button(self, 150 , 635, 370, 70, (0, 210, 210), hover_color=(159, 236, 238), function = self.intro_quit, text='QUIT')
        self.dead_buttons.append(dead_quit_button)

        back_to_intro = Button(self, 50 , 25, 250, 70, (255, 251, 101), hover_color=(255, 155, 155), function = self.back_to_intro, text='BACK TO HOME')
        self.scores_buttons.append(back_to_intro)
        clear_scores = Button(self, 350 , 25, 250, 70, (255, 251, 101), hover_color=(255, 155, 155), function = self.clear_scores, text='CLEAR SCORES')
        self.scores_buttons.append(clear_scores)

    def show_text(self, text, pos, size=20):
        self.game_font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', 28)
        text = self.game_font.render(text, True, BLACK)
        self.screen.blit(text, (pos[0], pos[1]))

    def reset(self):
        self.state = 'play'
        self.active_buttons = self.playing_buttons
        self.frame_count = 0
        self.snake = Snake(self)

    def view_scores(self):
        self.state = 'scores'
        self.active_buttons = self.scores_buttons

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            self.frame_count+=1
        
        pygame.quit()
        sys.exit()
    
    def get_events(self):
        if self.state == 'intro':
            self.intro_events()       
        if self.state == 'play':
            self.playing_events()       
        if self.state == 'dead':
            self.dead_events()
        if self.state == 'scores':
            self.scores_events() 
        
    def update(self):
        if self.state == 'intro':
            self.intro_update()
        if self.state == 'play':
            self.playing_update()       
        if self.state == 'dead':
            self.dead_update()       
        if self.state == 'scores':
            self.scores_update()
    
    def draw(self):
        self.screen.fill(BG_COL)
        if self.state == 'intro':
            self.intro_draw()
        if self.state == 'play':
            self.playing_draw()       
        if self.state == 'dead':
            self.dead_draw()        
        if self.state == 'scores':
            self.scores_draw()

        pygame.display.update()
    
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.intro_buttons:
                    if button.hovered:
                        button.click()

    def intro_update(self):
        for button in self.active_buttons:
            button.update()

    def intro_draw(self):
        tb_r = pygame.Rect(0, 0, 198, 254)
        self.screen.blit(self.intro_image, tb_r)

        for button in self.active_buttons:
            button.draw()
    
    def intro_to_play(self):
        self.state = 'play'
        self.active_buttons = self.playing_buttons

    def intro_quit(self):
        self.running = False

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_LEFT and self.snake.direction!=[1,0] :
                    self.snake.direction = [-1,0]
                if event.key == pygame.K_RIGHT and self.snake.direction!=[-1,0]:
                    self.snake.direction = [1, 0]
                if event.key == pygame.K_UP and self.snake.direction!=[0,1] :
                    self.snake.direction = [0, -1]
                if event.key == pygame.K_DOWN and self.snake.direction!=[0,-1] :
                    self.snake.direction = [0, 1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()

    def playing_update(self):
        for button in self.active_buttons:
            button.update()        
        self.game_window.update()
    
    def playing_draw(self):
        self.game_window.draw()
        for button in self.active_buttons:
            button.draw() 
        fruit_rect = pygame.Rect(75, 25, CELL_SIZE, CELL_SIZE)
        self.screen.blit(self.fruit, fruit_rect)
        self.show_text(str(self.snake.length-2), [125, 30])
         
    def playing_quit(self):
        self.running = False

    def dead_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()
    
    def dead_update(self):
        for button in self.active_buttons:
            button.update()
    
    def dead_draw(self):
        self.screen.fill((0,0,0))
        si_r = pygame.Rect(40,50, 198, 254)
        self.screen.blit(self.si, si_r)
        go_r = pygame.Rect(200, 200, 100, 100)
        self.screen.blit(self.go, go_r)
        t1 = pygame.Surface((660,20))
        t2 = pygame.Surface((660,20))
        t3 = pygame.Surface((20,750))
        t4 = pygame.Surface((20, 750))
        t1.fill((214, 214, 214))
        t2.fill((214, 214, 214))
        t3.fill((214, 214, 214))
        t4.fill((214, 214, 214))
        self.screen.blit(t1,(0,0))
        self.screen.blit(t2,(0,730))
        self.screen.blit(t3,(0,0))
        self.screen.blit(t4,(640,0))
        for button in self.active_buttons:
            button.draw()
    
    def scores_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()

    def scores_update(self):
        for button in self.active_buttons:
            button.update()

    def scores_draw(self):
        self.score_window.draw()
        for button in self.active_buttons:
            button.draw()
        for idx, score in enumerate(self.scores):
            y = idx*70+305
            self.show_text(str(score), [292, y], 35)

    def back_to_intro(self):
        self.state = 'intro'
        self.active_buttons = self.intro_buttons

    def clear_scores(self):
        self.scores = [0, 0, 0, 0, 0]
        with open(SAVES_FILE, 'w') as file:
            for score in self.scores:
                file.write(str(score)+'\n')