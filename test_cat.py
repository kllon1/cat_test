import pygame as py
from classes_meow import Player # Anim_stand, Block
from os import path
import pyganim

img_dir = path.join(path.dirname(__file__), 'img_cat')

WIDTH = 600
HEIGHT = 480
FPS = 60

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#инициализация pygame
py.init()
#sound
py.mixer.init()
# screen initialization
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('Cat_test')
icon = py.image.load('img_cat/icon_cat.png')
py.display.set_icon(icon)
clock = py.time.Clock()
press_keys = py.key.get_pressed()



all_sprites = py.sprite.Group()
player = Player()
# anim_stand = Anim_stand()
#block = Block()
all_sprites.add(player)
# all_sprites.add(anim_stand)
#all_sprites.add(block)


#загрузка графики
background = py.image.load(path.join(img_dir, 'forest.png')).convert()
background_mini_img = py.transform.scale(background, (600, 480))
background_mini_img.set_colorkey(BLACK)

cat_stand_anim = {}
cat_stand_anim['lg'] = []
for i in range(3):
    filename = f'cat_stand\cat_stand_{i}.png'
    img = py.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    cat_stand_anim['lg'].append(img)

#game cycle
running= True
while running:

    clock.tick(FPS)

    for event in py.event.get():
        #print(event)
        if event.type != py.KEYDOWN:
            pass
            # cat_anim_stand = Anim_stand(player.rect.center)
            # all_sprites.add(cat_anim_stand)
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                py.display.set_caption('MEOW')

        elif event.type == py.KEYUP:
            py.display.set_caption('Cat_test')
        if event.type == py.QUIT:
            running = False





    all_sprites.update()

    screen.fill(BLACK)
    screen.blit(background_mini_img, (0,0)) #вывод фона
    all_sprites.draw(screen)
    py.draw.rect(screen, BLUE, (140, 370, 75, 40)) #какой-то блок
    py.display.flip()

py.quit()