import pygame as pg
from sprites import *
 
class Game():
    def __init__(self): # kjører når vi starter spillet
        pg.init()
        self.color = (randint(0,255),randint(0,255),randint(0,255))

        self.WIDTH = 1200
        self.HEIGHT = 960

        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))
 
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 100)
        self.FPS = 120
        self.clock = pg.time.Clock()

        self.bg = pg.image.load("pg.jpg")
        
        
        self.new()
    
    def new(self): # ny runde, kjører feks når vi dør
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.projectiles_grp = pg.sprite.Group()
 
        self.hero = Player(self)
    
        self.all_sprites.add(self.hero)

        self.score = 0
        
        self.i = 0

        self.scoretext = self.comic_sans30.render(str(self.score), False, ((255,0,0)))
 
        self.run()
    
 
    def run(self): # mens vi spiller, game loop er her
        playing = True
        while playing: # game loop
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.new()
            
            self.screen.fill((0,0,0))

            self.prusektivcolide = pg.sprite.groupcollide(self.enemy_group,self.projectiles_grp,True,True)
            if self.prusektivcolide:  
                self.score += 1
                self.scoretext = self.comic_sans30.render(str(self.score), False, ((255,0,0)))


            self.colide = pg.sprite.spritecollide(self.hero,self.enemy_group,False)
            if self.colide:
                self.game_over_loop()

            # lag nye fiender 
            if len(self.enemy_group) < 3:
             enemy = Enemy()
             self.all_sprites.add(enemy)
             self.enemy_group.add(enemy)
 
            self.all_sprites.update() # kjør update funksjon til alle sprites i all_sprites gruppa
 
            # tegner alle sprites i gruppen all_sprites til screen
            self.all_sprites.draw(self.screen)

            self.screen.blit(self.scoretext,(10,10))

 
            # tegner HP tekst
            
            
            pg.display.update()
        
    def game_over_loop(self):
        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.comic_sans30.render("Game over, click R to restart", False, ((255,0,0)))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                       break
            self.screen.fill((0,0,0))
            self.screen.blit(self.game_over_text,(30,30))  # tegner tekst på skjerm. 
            self.screen.blit(self.bg,(1200,960))
            pg.display.update()

        self.new()  # starter ny runde      
        
g = Game() # her lages game classen, altså spillet starter