# File created by: Braeden Webb
# Agenda:
# GIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Braeden Webb
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import os
from os import path
# import settings 
from settings import *
from sprites import *
from math import *
from time import *
# from os import path

# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

### Images ###

# game_folder = os.path.dirname(__file__)
# print(game_folder)

# # Takes images from folders and sets them to variables
# ship_image = pg.image.load(os.path.join(game_folder, 'ship.png')).convert()

# # Set Image Transparency
# ship_image.set_colorkey(BLACK)

# # Does not store pixels but instead where they are and how many they are in dimensions
# # Allows for those values to changed and adjusted
# ship_image_rect = ship_image.get_rect()

# # Sets image coordinates
# # rps
# ship_image_rect.x = 0


### create game class in order to pass properties to the sprites file

class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
    def ticking(self):
        self.current_time = ((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
    def reset(self):
        self.event_time = ((pg.time.get_ticks())/1000)
    def gettime(self):
        self.current_time = self.delta()


class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("SERBIA STRONG")
        # Timer setd
        self.clock = pg.time.Clock()
        # Makes player running
        self.running = True
        self.get_current_time = True

    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "ship.png")).convert()        
        # self.bullet_img = pg.image.load(path.join(img_folder, "bullet.png")).convert()        
    def spawn_enemies(self):
        for i in range(1,14):
            # width, height, color
            m = Mob(30,30,(GREEN))
            # rantint sets direction
            # vec sets velocity between set range
            m.vel = vec(randint(1,5),randint(1,3))
            self.all_sprites.add(m)
            self.enemies.add(m)
    def spawn_enemies_less(self):
        for i in range(1,7):
            # width, height, color
            m = Mob(30,30,(GREEN))
            # rantint sets direction
            # vec sets velocity between set range
            m.vel = vec(randint(1,5),randint(1,3))
            self.all_sprites.add(m)
            self.enemies.add(m)
    def tough_spawn_enemies(self):
        for i in range(1,5):
            # width, height, color
            m = Mob(30,30,(LIGHT_BLUE))
            # rantint sets direction
            # vec sets velocity between set range
            m.vel = vec(randint(3,5),randint(1,6))
            self.all_sprites.add(m)
            self.enemies.add(m)
    # Properties for player
    def new(self):
        self.load_data()
        self.health = 100
        # standard score
        self.score = 0
        self.cd = Cooldown()
        # Time of death
        self.deathtime = 0
        # Player death
        self.playerdeath = False
        
        # self.all_sprites = pg.sprscoreoup()
        self.all_sprites = pg.sprite.Group()
        # self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.player = Player(self)    
        self.all_sprites.add(self.player)
        self.spawn_enemies()
        
        ### Sets Enemies ###
        # m = Mob(20,20,(GREEN))
        # self.all_sprites.add(m)
        # self.enemies.add(m)
        # m.vel = vec(5)
    
        # Makes game run
        self.run()
     
    # Makes game run
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    # Updates during Frames
    def update(self):
        self.all_sprites.update()
        # print(pg.time.get_ticks())
        # Checks if there are 0 enemies on screen
        if len(self.enemies) <= 2:
            # Spawns new enemies
            self.spawn_enemies()
            self.tough_spawn_enemies()
        hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            if hits[0]:
                # hits[0].kill()
                # print("enemy hit")
                # print(self.health)
                # Enemy damage
                self.health -= 1
        # Group collide checks if two variables collide
        # If they both collide and are set to True, they dissapear
        playerhits = pg.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if playerhits:
            if self.playerdeath == False:
                # Increase score
                self.score += 10

        # If player health goes below 0
        if self.health <= 0:
            self.playerdeath = True
            if self.get_current_time:
                self.deathtime = self.cd.delta
                self.get_current_time = False
        #     print("YOU LOSE:")
        #     print("YOUR TIME:")
        #     print(self.cd.delta)
        #     print("YOUR SCORE:")
        #     print(self.score)
            ### resets timer ###
            # self.cd.reset()

            # resets player position
            # self.playing = False

        # if self.health < 0:
        #     # Print Player Score
        #     print("YOUR TIME:")
        #     print(self.cd.delta)
        #     ### resets timer ###
        #     self.cd.reset()
        #     # resets player position
        #     self.playing = False


        # Starts ticking timer
        self.cd.ticking()

    # def draw(self):
    #     self.screen.fill(WHITE)
    #     self.all_sprites.draw(self.screen)
    #     pg.display.flip()
        
    # Text Properties
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('Retro Gaming')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    # Gets mouse
    # def get_mouse_now(self):
    #     x,y = pg.mouse.get_pos()
    #     return (x,y)
    
    # Draw Sceen Text
    def draw(self):
        self.screen.fill(BLACK)
        # draw players, enemies, etc...
        self.all_sprites.draw(self.screen)
        # draw standard text
        self.draw_text("HP: " + (str(self.health)), 42, RED, 100, HEIGHT/10)
        self.draw_text("SCORE: " + (str(self.score)), 42, BLUE, 160, 95)
        # self.draw_text("HIGH SCORE:", 42, YELLOW, 180, 130)
        self.draw_text("DEFEND SERBIA", 42, WHITE, WIDTH/2, 10)
        # draw health
        # self.draw_text(str(self.health), 42, RED, 150, HEIGHT/10)
        # draw timer
        self.draw_text(str(self.cd.delta), 42, WHITE, 120, 130)
        # draw score
        # self.draw_text(str(self.score), 42, BLUE, 250, 95)
        # Player death
        if self.playerdeath == True:
            self.screen.fill(RED) 
            # Draw text
            self.draw_text("SERBIA HAS FALLEN", 42, WHITE, WIDTH/2, 10)
            self.draw_text("YOUR SCORE: " + (str(self.score)), 42, WHITE, WIDTH/2, HEIGHT/2+50)
            self.draw_text("YOUR TIME: " + (str(self.deathtime)), 42, WHITE, WIDTH/2, HEIGHT/2+90)
            # Draw restart game text
            # self.draw_text("Press 'R' to Restart", 42, WHITE, WIDTH/2, HEIGHT/2+200)
            # Draws parameters
            # self.draw_text(str(self.score), 42, WHITE, WIDTH/3+250, HEIGHT/2+50)
            # self.draw_text(str(self.deathtime), 42, WHITE, WIDTH/3+250, HEIGHT/2+90)
        pg.display.flip()



# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()