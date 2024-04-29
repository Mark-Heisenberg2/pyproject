from pygame import *
from random import randint
from storage.counter import counter

window = display.set_mode((1000, 500))

play_button = image.load('storage/Play_button.png')
quit_button = image.load('storage/quit_button.png')
game_name = image.load('storage/Soccer Game.png')
plr = image.load('storage/placeholder.png')
feild = image.load('storage/feild.jpg')
feild = transform.rotate(feild, 90)
feild = transform.scale(feild, (1000, 500))
ball = image.load('storage/soccer-ball.png')
ball = transform.scale(ball, (30, 30))

class Spritec(sprite.Sprite):
    def  __init__(self, img: Surface, x, y, spd=0):
        self.image = img
        self.speed = spd
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Button(Spritec):
    def __init__(self, img, x, y, call):
        super().__init__(img, x, y)
        self.call = call

    def click(self):
        if self.rect.collidepoint(counter.click):
            self.call()

class Player(Spritec):
    def move(self):
        keys = key.get_pressed()

        if keys[K_s] and self.rect.bottom < window.get_height():
            self.rect.y += self.speed 

        elif keys[K_w] and self.rect.top > 0:
            self.rect.y -= self.speed

    def move2(self):
        keys = key.get_pressed()

        if keys[K_DOWN] and self.rect.bottom < window.get_height():
            self.rect.y += self.speed 

        elif keys[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed

class Ball(Spritec):
    def __init__(self, img: Surface, x, y, spdx=0, spdy=0):
        super().__init__(img, x, y)

        self.speedx = randint(-1, 1) * spdx
        self.speedy = randint(-1, 1) * spdy

        while self.speedx == 0 or self.speedy == 0:
            self.speedx = randint(-1, 1) * spdx
            self.speedy = randint(-1, 1) * spdy


    def move(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left <= 0:
            counter.plr2Scored += 1

            self.rect.x = window.get_width()/2
            self.rect.y = window.get_height()/2

        elif self.rect.right >= window.get_width():
            counter.plr1Scored += 1

            self.rect.x = window.get_width()/2
            self.rect.y = window.get_height()/2
        
        elif self.rect.bottom >= window.get_height():
            self.speedy *= -1

            counter.left_collid = True
            counter.right_collid = True

        elif self.rect.top <= 0:
            self.speedy *= -1

            counter.left_collid = True
            counter.right_collid = True
    
    def move_back(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left <= 0:
            self.speedx *= -1

        elif self.rect.right >= window.get_width():
            self.speedx *= -1

        
        elif self.rect.bottom >= window.get_height():
            self.speedy *= -1

            counter.left_collid = True
            counter.right_collid = True

        elif self.rect.top <= 0:
            self.speedy *= -1

            counter.left_collid = True
            counter.right_collid = True