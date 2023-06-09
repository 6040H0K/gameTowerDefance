from settings import *
import math

class Tower_area(pygame.Rect):
    def __init__(self, x_view, y_view):
        super().__init__(x_view, y_view, STEP, STEP)
        self.is_lock = False
        self.image = area_image
    def draw(self):
        window.blit(self.image, (self.x, self.y))

class Tower(pygame.Rect):
    def __init__(self,x, y, damage, image, attack_speed, tower_range, price):
        super().__init__(x, y, STEP, STEP)
        self.image = pygame.image.load(PATH + f'/images/towers/{image}.png')
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.image_standart = self.image
        self.image_body = pygame.image.load(PATH + f'/images/towers/turret.png')
        self.image_body = pygame.transform.scale(self.image_body, (self.width, self.height))
        self.damage = damage
        self.attack_speed = attack_speed
        self.count_attack = attack_speed
        self.price = price
        self.range = tower_range
        self.rotate_angle = 0
    def draw(self):
        window.blit(self.image_body, (self.x, self.y))
        window.blit(self.image, ((self.x - self.image.get_width() // 2) + STEP // 2, (self.y -  self.image.get_height() // 2) + STEP // 2))
    def fire(self,target):
        if not target.invulnerability:
            distance = (((self.x - target.x) ** 2) + ((self.y - target.y) ** 2)) ** 0.5
            if self.count_attack == 0:
                if distance <= self.range // 2:
                    rel_x, rel_y = target.x - self.x, target.y - self.y
                    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) 
                    self.image = self.image_standart 
                    self.image = pygame.transform.rotate(self.image, angle)
                    

                    target.hp -= self.damage
                    target.hp_rect.width = 40 / target.max_hp * target.hp 
                    self.count_attack = self.attack_speed
                    return True
            else:
                self.count_attack -= 1


class Tower_card(pygame.Rect):
    def __init__(self, image , x, y, width, height,damage,attack_speed,tower_range,price):
        super().__init__(x, y, width, height)
        self.name = image
        self.font = pygame.font.Font(os.path.join(PATH + '/fonts/Gilroy.otf'), 15)
        self.image = pygame.image.load(PATH + f'/images/towers/{image}_card.png')
        self.image = pygame.transform.scale(self.image, (self.width - 10, self.height - 10))
        self.image_body = pygame.image.load(PATH + f'/images/towers/turret.png')
        self.image_body = pygame.transform.scale(self.image_body, (self.width, self.height))
        self.damage = damage
        self.attack_speed = attack_speed
        self.tower_range = tower_range
        self.price = price
        self.background = pygame.image.load(PATH + f'/images/card.png')
        self.background = pygame.transform.scale(self.background, (100, 150))
        self.price_text = self.font.render(str(self.price), True, (255,255,255))
        self.attack_speed_text = self.font.render(str(4000 - self.attack_speed), True, (255,255,255))
        self.damage_text = self.font.render(str(self.damage), True, (255,255,255))

        
        self.damage_icon = pygame.image.load(PATH + f'/images/icons/damage.png')
        self.damage_icon = pygame.transform.scale(self.damage_icon, (20,20))
        self.price_icon = pygame.image.load(PATH + f'/images/icons/price.png')
        self.price_icon = pygame.transform.scale(self.price_icon, (20,20))
        self.speed_icon = pygame.image.load(PATH + f'/images/icons/speed.png')
        self.speed_icon = pygame.transform.scale(self.speed_icon, (20,20))
        self.range_icon = pygame.image.load(PATH + f'/images/icons/range.png')
        self.range_icon = pygame.transform.scale(self.range_icon, (20,20))

        self.range_text = self.font.render(str(self.tower_range), True, (255,255,255))
        self.name_text = self.font.render(self.name, True, (255,255,255))
        self.selected = False
        # damage atack_speed tower_range price
        
    def draw(self):
        if self.collidepoint(pygame.mouse.get_pos()) :
            window.blit(self.background, (self.x-12, self.y + 75))
            window.blit(self.name_text, (self.x + 37 - self.name_text.get_width() // 2, self.y + 100))
            window.blit(self.damage_text, (self.x + 20, self.y + 120))
            window.blit(self.damage_icon, (self.x - 5, self.y + 120))
            window.blit(self.attack_speed_text, (self.x + 20, self.y + 145))
            window.blit(self.speed_icon, (self.x - 5, self.y + 145))
            window.blit(self.range_text, (self.x + 20, self.y + 170))
            window.blit(self.range_icon, (self.x - 5, self.y + 170))
            window.blit(self.price_text, (self.x + 20, self.y + 195))
            window.blit(self.price_icon, (self.x - 5, self.y + 195))
        if self.selected:
            pygame.draw.rect(window,(0,255,0),self,5)
        window.blit(self.image_body, (self.x, self.y))
        window.blit(self.image,(self.x + 5,self.y + 5))
