

import pygame as pg

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)


screen = pg.display.set_mode((800,600))
player_img = pg.image.load("player.png")
player_img = pg.transform.scale(player_img,(100,130)) # endrer størrelse på player image
X = 50
Y = 50
speed = 4
direction_x = 1
direction_y = 1

FPS = 120
clock = pg.time.Clock()

box = pg.Rect(30,30,60,60,)
pg.draw.rect(screen, WHITE, box)

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False 
            
    screen.fill(WHITE)

    # move box 
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        Y -= speed
    if keys[pg.K_s]:
        Y += speed
    if keys[pg.K_a]:
        X -= speed
    if keys[pg.K_d]:
        X += speed



    if X > 700:
        X = 700
    if X < 0:
      X = 0

    if Y > 500:
        Y = 500
    if Y < 0: 
        Y = 0
        



    box = pg.Rect(X,Y,100,100,) 
    pg.draw.rect(screen, BLACK, box) # tegner box

    screen.blit(player_img, (X,Y))

    pg.display.update()