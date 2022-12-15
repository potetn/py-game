from ast import Not
from tkinter import Y
from turtle import filling
import pygame as pg
from random import randint
vec = pg.math.Vector2
 
player_img = pg.image.load("player.png")
player_img = pg.transform.scale(player_img,(100,130)) # endrer størrelse på player image
player_img_left = pg.transform.flip(player_img, True,False)

enemy_img = pg.image.load("zombie old lady.png")
enemy_img = pg.transform.scale(enemy_img,(100,130)) # endrer størrelse på player image
enemy_img_left = pg.transform.flip(enemy_img, True,False)

 

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self) 
        self.image = player_img
        self.rect = self.image.get_rect() # henter self.imag sin størelse og lager en hitbox
        self.pos = vec(100,130)
        self.rect.center = self.pos
        self.speed = 3
        self.energy = 100
        self.game = game        
        self.projectile_speed = 5
        self.attack_direction_x = 1
        self.attack_direction_y = 0

        self.energy = 50
        
   
    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
           self.pos.y -= self.speed       
        if keys[pg.K_s]:
          self.pos.y += self.speed    
        if keys[pg.K_a]:
          self.pos.x -= self.speed       
        if keys[pg.K_d]:
          self.pos.x += self.speed  
        
        self.rect.center = self.pos # flytter rect til player til ny posisjon hver frame
        print(self.energy)

        if keys[pg.K_a]:
            self.image = player_img_left # sett self.image til bildet som peker til venstre
            self.pos.x -= self.speed

        if keys[pg.K_d]:
            self.image = player_img # sett self.image til bildet som peker til venstre  
            self.pos.x += self.speed

        if keys[pg.K_s]:
            self.image = player_img # sett self.image til bildet som peker til venstre  
            self.pos.y += self.speed
        
        if keys[pg.K_w]:
            self.image = player_img # sett self.image til bildet som peker til venstre  
            self.pos.y -= self.speed
       
        if keys[pg.K_SPACE] and self.energy >= 50:
            self.energy = 0
            self.attack()

        self.energy += 1

    def attack(self):
     Ranged_attack(self.game, self.pos.x, self.pos.y, self.attack_direction_x, self.attack_direction_y)
 



# egen klasse for ranged attack
class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, x ,y, direction_x, direction_y):
        self.groups = game.all_sprites, game.projectiles_grp # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface([50,50])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) # start posisjon
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.rect.center = self.pos
 
    def update(self):
        self.rect.center = self.pos
        self.pos.x += self.direction_x
        self.pos.y += self.direction_y

        # hvis self pos x er større enn > bredden på skjerm, kjør self.kill()
        if self.pos.x > 1200:
          self.kill()
 
# bestemmer fart til ranged attack
 
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img_left
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox
        self.pos = vec(1400,randint(0,900))
        self.rect.center = self.pos
        self.speed = 2
        
    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon hver frame
 
        self.pos.x -= self.speed
 
        if self.pos.x < -100: # til venstre for skjermen
            self.pos.x = 1400
            self.pos.y = randint(0,900)