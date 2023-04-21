# File created by: Braeden Webb

import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint

vec = pg.math.Vector2

# player class
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    # Player Inputs
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print("PAUSED")
        #     else:
        #         PAUSED = False
        #         print("PAUSED")
        if keystate[pg.K_r]:
            self.playing = False
    # Player Bullet shoot
    def shoot(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE]:
            self.acc.x = -PLAYER_ACC
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.0 * self.acc
        self.rect.midbottom = self.pos
        # checks if player is off screen
        if self.rect.x > WIDTH:
            # print("bump")
            self.vel.x = -5
        if self.rect.x < 0:
            # print("bump")
            self.vel.x = 5
        if self.rect.y < 0:
            # print("bump")
            self.vel.y = 5
        if self.rect.y > HEIGHT:
            # print("bump")
            self.vel.y = -5
            


class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/1)
        # mob speed
        self.vel = vec(5)
        self.acc = vec(1,1)
        self.cofric = 0.01
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

# playerbullet

class Bullet(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((25,25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False