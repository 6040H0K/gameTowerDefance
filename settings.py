import os
import pygame

pygame.init()

PATH = os.path.abspath(__file__ + '/..')
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
STEP = 50

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TowerDefense')

map = [
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['3','l','l','l','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','u','0','0','0','0','0','0','0','0','d','l','l','l','0','0','0','0'],
    ['0','r','r','u','0','d','l','l','l','0','0','0','d','0','0','u','0','0','0','0'],
    ['0','u','1','0','0','d','0','0','u','0','0','0','d','0','0','u','0','0','0','0'],
    ['0','u','0','0','0','d','0','1','u','0','0','0','d','0','0','u','0','0','0','0'],
    ['0','u','l','l','l','l','0','0','u','0','0','0','d','1','0','u','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','u','l','l','l','l','0','0','u','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','u','1','0','0','0'],
    ['0','0','0','r','r','r','r','d','0','r','r','r','r','r','r','u','0','0','0','0'],
    ['0','0','0','u','0','1','0','d','0','u','1','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','u','0','0','0','d','0','u','l','l','l','l','l','l','0','0','0','0'],
    ['2','r','r','u','0','0','0','d','0','0','0','0','0','0','0','u','0','0','0','0'],
    ['0','0','0','0','0','0','0','r','r','r','r','r','r','r','r','u','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
]

image_road = pygame.image.load(PATH + '/images/main/road.png')
image_road = pygame.transform.scale(image_road, (STEP,STEP))
area_image = pygame.image.load(PATH + '/images/main/area.png')
area_image = pygame.transform.scale(area_image, (STEP,STEP))
grass_image = pygame.image.load(PATH + '/images/main/grass.png')
grass_image = pygame.transform.scale(grass_image, (STEP,STEP))
coin_image = pygame.image.load(PATH + '/images/coin.png')
coin_image = pygame.transform.scale(coin_image, (30,30))

finish_font = pygame.font.Font(os.path.join(PATH, 'fonts/Gilroy.otf'), 100)
text_win = finish_font.render("ПЕРЕМОГА",True,(0, 160, 0),(156,156,156))
text_lose = finish_font.render("ПОРАЗКА",True,(255,0,0),(156,156,156))

bg_music = pygame.mixer.Sound(os.path.join(PATH, 'sounds/music.wav'))
bg_music.set_volume(0.1)
bg_music.play(-1)

