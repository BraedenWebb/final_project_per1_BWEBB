# File created by: Braeden Webb
# Agenda:
# gIT GITHUB    
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
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

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
        # print(self.delta)
    def timer(self):
        self.current_time = ((pg.time.get_ticks())/1000)

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("D_O_D_G_E")
        # Timer set
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        ## starting a new game
        self.health = 100
        self.cd = Cooldown()
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)    
        self.all_sprites.add(self.player)
        # adds enemies
        for i in range(1,10):
            # widht, height, color
            m = Mob(20,20,(RED))
            # vec sets velocity between set range
            # rantint sets direction
            m.vel = vec(randint(1,10),randint(1,5))
            self.all_sprites.add(m)
            self.enemies.add(m)
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
        # Starts ticking timer
        self.cd.ticking()
        # print(pg.time.get_ticks())
        hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            if hits[0]:
                # hits[0].kill()
                print("enemy hit")
                print(self.health)
                # Enemy damage
                self.health -= 1
        # If player health goes below 0
        if self.health == 0:
            # resets player position
            self.playing = False
            ### resets timer ###

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('Retro Gaming')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
    
    # Sceen text
    def draw(self):
        self.screen.fill(WHITE)
        self.draw_text("HP:", 42, RED, 60, HEIGHT/10)
        # draw health
        self.draw_text(str(self.health), 42, RED, 150, HEIGHT/10)
        # draw timer
        self.draw_text(str(self.cd.delta), 42, BLACK, WIDTH/1.15, HEIGHT/10)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()