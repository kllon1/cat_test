import pygame
from os import path


img_dir = path.join(path.dirname(__file__), 'img_cat')
WIDTH = 600
HEIGHT = 480
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

player_stand = [
    pygame.image.load(path.join(img_dir, 'cat_stand\cat_stand_0.png')),
    pygame.image.load(path.join(img_dir, 'cat_stand\cat_stand_1.png')),
    pygame.image.load(path.join(img_dir, 'cat_stand\cat_stand_2.png')),
    pygame.image.load(path.join(img_dir, 'cat_stand\cat_stand_3.png'))
    ]
player_anim_count = 0

player_walk_l = [
    pygame.image.load(path.join(img_dir, 'cat_walk_l\cat_walk_1_l.png')),
    pygame.image.load(path.join(img_dir, 'cat_walk_l\cat_walk_2_l.png')),
    pygame.image.load(path.join(img_dir, 'cat_walk_l\cat_walk_3_l.png'))
    ]
player_walk_l_count = 0

player_walk_r = [
    pygame.image.load(path.join(img_dir, 'cat_walk_r\cat_walk_1_r.png')),
    pygame.image.load(path.join(img_dir, 'cat_walk_r\cat_walk_2_r.png')),
    pygame.image.load(path.join(img_dir, 'cat_walk_r\cat_walk_3_r.png'))
    ]
player_walk_r_count = 0
# cat_stand_anim = {}
# cat_stand_anim['lg'] = []
# for i in range(4):
#     filename = f'cat_stand\cat_stand_{i}.png'
#     img = pygame.image.load(path.join(img_dir, filename))
#     img.set_colorkey(BLACK)
#     cat_stand_anim['lg'].append(img)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.transform.scale(player_stand[3], (45, 50))
        #self.image = player_stand[3]
        self.image = pygame.Surface((10, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 430)

        self.is_jump = False #прыжок
        self.jump_count = 9
        # self.player_anim_count = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 35


    def update(self):
        now = pygame.time.get_ticks()
        self.speedx = 0
        self.speedy = 0
        global player_anim_count
        global player_walk_l_count
        global player_walk_r_count

        keystate = pygame.key.get_pressed()
        # self.image = player_stand[player_anim_count]
        # if player_anim_count == 3:
        #     player_anim_count = 0
        # else:
        #     player_anim_count += 1
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if keystate[pygame.K_UP]:
                #self.image = pygame.transform.scale(player_stand[self.player_anim_count], (45, 50))
                self.image = player_stand[player_anim_count]
                if player_anim_count == 3:
                    player_anim_count = 0
                    self.frame = 0
                else:
                    player_anim_count += 1


            if keystate[pygame.K_LEFT]:
                self.speedx = -10
                self.image = player_walk_l[player_walk_l_count]
                if player_walk_l_count == 2:
                    player_walk_l_count = 0
                    self.frame = 0
                else:
                    player_walk_l_count += 1
            if keystate[pygame.K_RIGHT]:
                self.speedx = 10
                self.image = player_walk_r[player_walk_r_count]
                if player_walk_r_count == 2:
                    player_walk_r_count = 0
                    self.frame = 0
                else:
                    player_walk_r_count += 1
        # if keystate[pygame.K_UP]:
        #     self.speedy = -8
        # if keystate[pygame.K_DOWN]:
        #     self.speedy = 8
#прыжок
        if not self.is_jump:
            if keystate[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -9:
                if self.jump_count > 0:
                    self.rect.y -= (self.jump_count ** 2) // 2
                else:
                    self.rect.y += (self.jump_count ** 2) // 2
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 9

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


# class Block(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((60, 20))
#         self.image.fill(BLUE)
#         self.rect = self.image.get_rect()
#         self.rect.center = (100, 400)


class Anim_stand(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = cat_stand_anim['lg'][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 70


    def update(self):
        now = pygame.time.get_ticks()
        keystate = pygame.key.get_pressed()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if keystate[pygame.K_LEFT] or keystate[pygame.K_RIGHT] or keystate[pygame.K_SPACE]:
                self.kill()
            if self.frame == len(cat_stand_anim['lg']):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = cat_stand_anim['lg'][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

