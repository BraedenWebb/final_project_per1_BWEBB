# File created by: Braeden Webb
# Sources: https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5F2023%5FSpring%2FCode%2Fexamples%2Fgame%5Fexample%2Fmain%2Epy&parent=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5F2023%5FSpring%2FCode%2Fexamples%2Fgame%5Fexample


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
        
        # Adds Images
        self.images_orig = pg.transform.scale(self.player_ship, (50,50))
        self.image_orig.set_colorkey(WHITE)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()

        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/4, HEIGHT/1.1)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.fired = False
    
    # Player Inputs
    def input(self):
        keystate = pg.key.get_pressed()
        # Vertical Controls
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        # Horizontal Controls
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # Firing Controls
        if keystate[pg.K_SPACE]:
            self.fire()
            # print("bullet fired")

    # Player Bullet shoot
    def fire(self):
        # self.current_time = (pg.time.get_ticks()/1000)
        # mpos = pg.mouse.get_pos()
        # targetx = mpos[0]
        # targety = mpos[1]
        # distance_x = targetx - self.rect.x
        # distance_y = targety - self.rect.y
        speed_x = 0 
        speed_y = -10
        # print(speed_x)
        b = Bullet(self.pos.x,self.pos.y - self.rect.height, 30, 30, speed_x, speed_y, "player")
        # else:
        #     p = Pewpew(self.pos.x,self.pos.y - self.rect.height, 10, 10, speed_x, speed_y, "player")

        # Creates sprites
        self.game.all_sprites.add(b)
        self.game.bullets.add(b)

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
        # self.vel = vec(1)
        # self.acc = vec(1,1)
        # self.cofric = 0.001
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

# bullet sprite
class Bullet(Sprite):
    def __init__(self, x, y, w, h,sx,sy, owner):
        Sprite.__init__(self)
        self.owner = owner
        self.image = pg.Surface((w, h))

        # Sets bullet sprite
        # self.image = pg.transform.scale(self.game.bullet_img, (15,15))
        # self.image.set_colorkey(WHITE)

        # self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.image = pg.Surface((15,15))

        self.rect.x = x
        self.rect.y = y
        self.speed_x = sx
        self.speed_y = sy
        self.fired = False
        # Bullet color
        self.image.fill(RED)
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bullet enemy collision
        # Destroys bullet
        # bullethits = pg.sprite.spritecollide(self.enemies, False)
        # if bullethits:
        #     self.kill()
        #     print("test")
            
    #     if self.owner == "player":
    #         self.rect.x += self.speed_x
    #         self.rect.y += self.speed_y
    #         # print(pewpews)
    #     else:
    #         self.rect.y += self.speed_y
    #     if (self.rect.y < 0 or self.rect.y > HEIGHT):
    #         self.kill()
            # print(pewpews)