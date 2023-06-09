from settings import *
from random import randint

class Enemy(pygame.Rect):
    def __init__(self, hp, speed, coin, image, x_view, y_view, x_matrix, y_matrix, template_count_step, spawn_count):
        super().__init__(x_view, y_view, STEP, STEP)
        # image = 1
        self.image = pygame.image.load(PATH + f'/images/enemies/zombie{image}-1.png')
        self.image = pygame.transform.scale(self.image, (STEP,STEP))
        self.image1 = pygame.image.load(PATH + f'/images/enemies/zombie{image}-2.png')
        self.image1 = pygame.transform.scale(self.image1, (STEP,STEP))
        self.image_right_1 = pygame.transform.flip(self.image,True, False)
        self.image_left_1 = self.image
        self.image_right_2 = pygame.transform.flip(self.image1,True, False)
        self.image_left_2 = self.image1
        self.skin = 0
        self.speed = STEP
        self.hp = hp
        self.max_hp = hp
        self.coin = coin
        self.x_matrix = x_matrix
        self.y_matrix = y_matrix
        self.template_count_step = template_count_step
        self.spawn_count = spawn_count
        self.count_step = template_count_step
        self.count_moving = 0
        self.template_count_moving = 25
        self.hp_bar = pygame.Rect(self.x + 5, self.y - 10, 40, 6)
        self.hp_rect = pygame.Rect(self.x + 5, self.y - 10, 40, 6)
        self.damage_to_pixel = 40 - (((hp - 1) * 40) /  hp )
        self.rotation_side = "left"
        self.invulnerability = True
        self.count_skin = 0
        self.coin_y = None
        self.dead_count = -1
    def move(self):
        if self.count_step == 0:
            if self.invulnerability:
                self.invulnerability = False
            direction = map[self.y_matrix][self.x_matrix]
            # u d r l
            if direction == 'u':
                if self.count_moving != self.template_count_moving:
                    self.y -= self.speed // self.template_count_moving
                    if self.skin == 0:
                        if self.rotation_side == "right":
                            self.image = self.image_right_1
                        elif self.rotation_side == "left":
                            self.image = self.image_left_1
                    elif self.skin == 1:
                        if self.rotation_side == "right":
                            self.image = self.image_right_2
                        elif self.rotation_side == "left":
                            self.image = self.image_left_2
                    self.count_moving += 1
                else:
                    self.y_matrix -= 1
                    self.count_moving = 0
            elif direction == 'd':
                if self.count_moving != self.template_count_moving:
                    self.y += self.speed // self.template_count_moving
                    if self.skin == 0:
                        if self.rotation_side == "right":
                            self.image = self.image_right_1
                        elif self.rotation_side == "left":
                            self.image = self.image_left_1
                    elif self.skin == 1:
                        if self.rotation_side == "right":
                            self.image = self.image_right_2
                        elif self.rotation_side == "left":
                            self.image = self.image_left_2
                    self.count_moving += 1
                else:
                    self.y_matrix += 1
                    self.count_moving = 0
            elif direction == 'l':
                if self.count_moving != self.template_count_moving:
                    if self.skin == 0:
                        self.image = self.image_left_1
                    else: 
                        self.image = self.image_left_2
                    self.rotation_side = "left"
                    self.x -= self.speed // self.template_count_moving
                    self.count_moving += 1
                else:
                    self.x_matrix -= 1
                    self.count_moving = 0
            elif direction == 'r':
                if self.count_moving != self.template_count_moving:
                    if self.skin == 0:
                        self.image = self.image_right_1
                    else: 
                        self.image = self.image_right_2
                    self.rotation_side = "right"
                    self.x += self.speed // self.template_count_moving
                    self.count_moving += 1
                else:
                    self.x_matrix += 1
                    self.count_moving = 0
            self.count_step = self.template_count_step
            self.hp_bar.x = self.x + 5
            self.hp_bar.y = self.y - 10
            self.hp_rect.x = self.x + 5
            self.hp_rect.y = self.y - 10
        else:
            self.count_step -= 1

    def draw(self):
        if self.spawn_count == 0:
            # self.attack()
            # print(self.x_matrix, self.y_matrix)
            if self.count_skin == 0:
                if self.skin == 0:
                    self.skin = 1
                else:
                    self.skin = 0
                self.count_skin = 50
            else:
                self.count_skin -= 1
            if self.dead_count == -1: 
                self.move()
            else:
                window.blit(coin_image, (self.x + 10, self.coin_y))
            window.blit(self.image, (self.x, self.y))
            pygame.draw.rect(window, (0,0,0), self.hp_bar)
            pygame.draw.rect(window, (255,0,0), self.hp_rect)
        else:
            self.spawn_count -= 1

    # def attack(self):
    #     if randint(1,10) == 1:
    #         damage = randint(1,10)
    #         self.hp -= damage
    #         self.hp_rect.width -= damage * self.damage_to_pixel
# [  ]