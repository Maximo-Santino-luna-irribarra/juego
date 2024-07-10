import pygame 
pygame.font.init()

WIDTH = 1344#ancho
HEIGHT = 619#alto
WIDTH_PJ = 60
HEIGHT_PJ =  40
WIDTH_ENEMY_PISO = 50
HEIGHT_ENEMY_PISO =  50
WIDTH_ENEMY_aire = 30
HEIGHT_ENEMY_aire =  30
WIDTH_cuadradito_de_vida = 30
HEIGHT_cuadradito_de_vida =  30
FPS = 60
VELOICIDAD = 3
escala_pj = 1.2
escala_enemigo = 1
GRAVITY = 1
jump_speed = 20
VELOICIDAD_ENEMY_PISO = 3
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
VIOLET = (74, 40, 130)
TRANSPARENCY = 80
colors = [RED, BLUE, GREEN, LIGHT_BLUE, WHITE, YELLOW, ORANGE, VIOLET]
screen_principal = pygame.display.set_mode((WIDTH, HEIGHT))
cantidad_de_veces_clikeada = 0
font = pygame.font.Font("source\Minercraftory.ttf",36)





