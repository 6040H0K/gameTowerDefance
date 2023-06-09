from settings import *
from enemies import *
from towers import *
from random import randint

class Cursor:
    def __init__(self, image):
        self.x = 0
        self.y = 0
        self.tower_name = None
        self.image = pygame.image.load(PATH + f'/images/{image}.png')
        self.image = pygame.transform.scale(self.image,(26,26))
    def get_cors(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.lbm, self.mbm, self.rbm = pygame.mouse.get_pressed()
    def choose_card(self, card):
        if card.collidepoint(self.x, self.y) and self.lbm:
            self.tower_name = card.name
            self.damage = card.damage
            self.attack_speed = card.attack_speed
            self.tower_range = card.tower_range
            self.price = card.price
            
            for card1 in cards_list:
                card1.selected = False
            card.selected = True

    def place_tower(self, area):
        if area.collidepoint(self.x, self.y) and self.lbm:
            if not area.is_lock and self.tower_name:
                if self.price <= castles_list[0].coin:
                    castles_list[0].coin -= self.price
                    area.is_lock = True
                    towers_list.append(Tower(
                        area.x, 
                        area.y, 
                        self.damage, 
                        self.tower_name,
                        self.attack_speed,
                        self.tower_range,
                        self.price
                        )
                    )
    def draw(self):
        window.blit(self.image,(self.x - 13,self.y - 13))
        
pygame.mouse.set_visible(False)

class Road(pygame.Rect):
    def __init__(self, x,y,type_road):
        super().__init__(x,y,STEP,STEP)
        if type_road == 1:
            self.image = image_road
        else:
            self.image = grass_image

    def draw(self):
        window.blit(self.image, (self.x, self.y))
    


class Castle(pygame.Rect):
    def __init__(self,x_view, y_view, hp, coin, income_coin, type_castle):
        super().__init__(x_view, y_view, STEP, STEP)
        self.hp = hp
        self.coin = coin
        self.income_coin = income_coin
        self.type_castle = type_castle
        if type_castle == 1:
            self.image = pygame.image.load(PATH + '/images/main/castle.png')
        else:
            self.image = pygame.image.load(PATH + '/images/main/enemy_castle.png')
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
    def draw(self):
        window.blit(self.image, (self.x, self.y))

towers_list = []
road_list = []
grass_list = []
area_list = []
castles_list = []
enemies_list = []
cards_list = []

cards_list.append(Tower_card('turret_tower',900,10,75,75,5,500,200,150))
cards_list.append(Tower_card('v2_tower',800,10,75,75,9,600,400,350))
cards_list.append(Tower_card('shot_gunner',700,10,75,75,75,5000,200,450))

class Coins_text:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.font = pygame.font.Font(os.path.join(PATH + '/fonts/Gilroy.otf'), 40)
        # w = 125
        # h = 31.25
        # padding = 27
        self.background = pygame.image.load(PATH + '/images/money.png')
        self.background = pygame.transform.scale(self.background, (250,64))
        self.text = self.font.render(str(castles_list[0].coin),True, (77, 77, 77))
    def draw(self):
        window.blit(self.background, (self.x, self.y))
        self.text = self.font.render(str(castles_list[0].coin),True, (77, 77, 77))
        window.blit(self.text, (self.x + 56, self.y + 9))

spawn_timeout = 0
step_timeout_delta = 10
for i in range(50):
    print(spawn_timeout)
    step_timeout = step_timeout_delta
    if i < 10:
        enemies_list.append(Enemy(50,50,20,'1',50,13*50,1,13,step_timeout, spawn_timeout))
    elif i < 20:
        if i == 10:
            spawn_timeout += 5000
        enemies_list.append(Enemy(100,50,30,'2',50,13*50,1,13,step_timeout, spawn_timeout))
    elif i < 30:
        if i == 20:
            spawn_timeout += 5000
            step_timeout_delta = 5
            step_timeout -= 5
        enemies_list.append(Enemy(100,50,40,'3',50,13*50,1,13,step_timeout, spawn_timeout))
    elif i < 40:
        if i == 30:
            spawn_timeout += 5000
            step_timeout_delta = 15
            step_timeout += 10
        enemies_list.append(Enemy(300,50,50,'4',50,13*50,1,13,step_timeout, spawn_timeout))
    elif i <= 50:
        if i == 40:
            spawn_timeout += 5000
            step_timeout_delta = 20
            step_timeout += 5
        enemies_list.append(Enemy(450,50,60,'5',50,13*50,1,13,step_timeout, spawn_timeout))
    spawn_timeout += step_timeout + 500

x = 0
y = 0
for idxy, i in enumerate(map):
    for idx, j in enumerate(i):
        if j == 'u' or j == 'd' or j == 'r' or j == 'l':
            road_list.append(Road(x,y,1))
        elif j == '0':
            grass_list.append(Road(x,y,2))
        elif j == '1':
            area_list.append(Tower_area(x,y))
        elif j == '2':
            castles_list.append(Castle(x,y,100,150,10,2))
        elif j == '3':
            castles_list.append(Castle(x,y,100,150,10,1))
        x += STEP
    x = 0
    y += STEP

game_run = True
coins = Coins_text()
cursor = Cursor('cursor')
game_finished = False
for castle in castles_list:
    if castle.type_castle == 1:
        castle_id = castles_list.index(castle)
        break

while game_run:
    window.fill((0,0,0))
    for road in road_list:
        road.draw()
    for castle in castles_list:
        castle.draw()
    for grass in grass_list:
        grass.draw()
    for tower_area in area_list:
        tower_area.draw()
        cursor.place_tower(tower_area)
    for tower in towers_list:
        for enemy in enemies_list:
            if tower.fire(enemy):
                break
        tower.draw()
    for card in cards_list:
        card.draw()
        cursor.choose_card(card)
    for enemy in enemies_list:
        enemy.draw()
        if enemy.hp <= 0:
            if enemy.dead_count == -1:
                castles_list[0].coin += enemy.coin
                enemy.coin_y = enemy.y
                enemy.dead_count = 200
            elif enemy.dead_count > 0:
                enemy.coin_y -= 1
                enemy.dead_count -= 1
            else:
                enemies_list.remove(enemy)
        elif enemy.colliderect(castles_list[castle_id]):
            game_run = False
            game_finished = True
            finish_status = False
    coins.draw()
    if len(enemies_list) == 0:
        game_run = False
        game_finished = True
        finish_status = True 
        # WIN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    cursor.get_cors()
    cursor.draw()
    pygame.display.flip()

while game_finished:
    window.fill((0,0,0))
    for road in road_list:
        road.draw()
    for castle in castles_list:
        castle.draw()
    for grass in grass_list:
        grass.draw()
    for tower_area in area_list:
        tower_area.draw()
    for tower in towers_list:
        tower.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = False
    if finish_status:
        window.blit(text_win, (SCREEN_WIDTH // 2 - text_win.get_width() // 2, SCREEN_HEIGHT // 2 - text_win.get_height() // 2))
    else:
        window.blit(text_lose, (SCREEN_WIDTH // 2 - text_lose.get_width() // 2, SCREEN_HEIGHT // 2 - text_lose.get_height() // 2))
    cursor.get_cors()
    cursor.draw()
    pygame.display.flip()


