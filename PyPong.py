import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from pygame.mixer import *
from random import *

linkMusic = "D:/cd/Python/CODE/PyPong-Game/Rubik.mp3"

class RectangularSprite(Sprite):   
    def __init__(self, size, center):
        Sprite.__init__(self)
        self.image = Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = center   
    def up_paddle(self):
        self.rect = self.rect.move(0, -5)
        screen.fill((0,0,0))
        if collide_rect(self, border_top):
            self.rect.top = 10      
    def down_paddle(self):
        self.rect = self.rect.move(0, 5) 
        screen.fill((0,0,0))
        if collide_rect(self, border_bottom):
            self.rect.bottom = 475
class Banner(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        my_font = pygame.font.SysFont(None, 30)
        self.image = my_font.render("MUSIC", True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 30)

#music
mixer.init()            # initialize sound system
music.load(linkMusic)   # load bg music file
music.play(loops=-1)    # play/loop music

# main
pygame.init()
display.set_caption("PyPong Game")
screen = display.set_mode((800, 480))
border_top = RectangularSprite((1600,15),(0,0))
border_bottom = RectangularSprite((1600,15),(0,480))
border_left = RectangularSprite((15,960),(0,0))
border_right = RectangularSprite((15,960),(800,0))
paddle_left = RectangularSprite((20,150),(25,240))
paddle_right = RectangularSprite((20,150),(775,240))
ball = RectangularSprite((15,15),(400,240))
musik = Banner()
all_sprites = Group(border_top, border_bottom, border_left, border_right, paddle_left, paddle_right, ball, musik)
score_font = pygame.font.SysFont(None, 72)
time.set_timer(USEREVENT, 20)

#init
up = 1
down = -1
left = -2
right = 2
x = 5
y = 5
direct = up
score1, score2 = 0, 0
music_on = True
music_off = False
toggle_music = music_on

while True:
    score = score_font.render((str(score1) + ":" + str(score2)), True, (255, 255, 255))
    screen.blit(score, (380, 20))
    all_sprites.draw(screen)
    display.update()

    ev = event.wait() # wait for an event
    if ev.type == QUIT:
        pygame.quit()
        break
    elif ev.type == USEREVENT:      
        if direct == up:
            ball.rect = ball.rect.move(x, -5) 
            screen.fill((0,0,0))
            if collide_rect(ball, border_top):
                direct = down
                x = choice(range(-5,15,10)) 
            elif collide_rect(ball, paddle_right):
                direct = left
                y = choice(range(-5,15,10))
            elif collide_rect(ball, paddle_left):
                y = choice(range(-5,15,10))
                direct = right
        elif direct == down:
            ball.rect = ball.rect.move(x, 5) 
            screen.fill((0,0,0))
            if collide_rect(ball, border_bottom):               
                direct = up
                x = choice(range(-5,15,10)) 
            elif collide_rect(ball, paddle_right):
                direct = left
                y = choice(range(-5,15,10))
            elif collide_rect(ball, paddle_left):
                direct = right
                y = choice(range(-5,15,10))
        elif direct == left:
            ball.rect = ball.rect.move(-5, y) 
            screen.fill((0,0,0))
            if collide_rect(ball, border_bottom):
                direct = up
                x = choice(range(-5,15,10)) 
            elif collide_rect(ball, border_top):
                direct = down
                x = choice(range(-5,15,10)) 
            elif collide_rect(ball, paddle_left):
                direct = right
                y = choice(range(-5,15,10))
        elif direct == right:
            ball.rect = ball.rect.move(5, y) 
            screen.fill((0,0,0))
            if collide_rect(ball, border_bottom):
                direct = up
                x = choice(range(-5,15,10)) 
            elif collide_rect(ball, border_top):
                direct = down
                x = choice(range(-5,15,10)) 
            elif collide_rect(ball, paddle_right):
                direct = left   
                y = choice(range(-5,15,10)) 
        if collide_rect(ball, border_right):  
            score1 += 1
            x = -5
            y = choice(range(-5,15,10))
            direct = choice(range(-1,3,2))          
        elif collide_rect(ball, border_left): 
            score2 += 1   
            x = 5
            y = choice(range(-5,15,10))
            direct = choice(range(-1,3,2))   
    elif ev.type == KEYDOWN:
        if ev.key == K_UP:
            paddle_right.up_paddle()
        elif ev.key == K_DOWN:
            paddle_right.down_paddle()
        elif ev.key == K_w:
            paddle_left.up_paddle()
        elif ev.key == K_s:
            paddle_left.down_paddle()
    elif ev.type == MOUSEBUTTONDOWN:
        if musik.rect.collidepoint(mouse.get_pos()):
            toggle_music = not toggle_music
            if toggle_music == music_on:
                music.play(loops=-1) # play/loop music
            elif toggle_music == music_off:
                music.stop()