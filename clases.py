import pygame
from constantes import*
from random import *
from funciones import *
class Personaje():
    
    def __init__(self, x, y,animaciones):
        self.flip = False   
        self.animacion= animaciones 
        self.frame = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame]
        self.forma = pygame.Rect(0, 0,WIDTH_PJ,HEIGHT_PJ)
        self.forma.center = (x, y)



    def update(self):
        cooldown_animacion = 100
        self.image = self.animacion[self.frame]
        if pygame.time.get_ticks() - self.update_time >=cooldown_animacion:
            self.frame = self.frame + 1
            self.update_time = pygame.time.get_ticks()
            
        if self.frame >= len(self.animacion):
            self.frame = 0

    def movimiento(self,delta_x, delta_y,screen_WIDTH,screen_HEIGHT):
        nueva_x = self.forma.x + delta_x
        nueva_y = self.forma.y + delta_y
       
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
    
        if nueva_x < 0:
            nueva_x = 0
        elif nueva_x + WIDTH_PJ > screen_WIDTH:
            nueva_x = screen_WIDTH - WIDTH_PJ
            
        
        if nueva_y < 0:
            nueva_y = 0
        elif nueva_y + HEIGHT_PJ > screen_HEIGHT:
            nueva_y = screen_HEIGHT -HEIGHT_PJ
        self.forma.x = nueva_x
        self.forma.y = nueva_y

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        
    



class Enemigos_voladores:
    def __init__(self, url_imagen):
        self.enemigo_width = WIDTH_ENEMY_aire
        self.enemigo_height = HEIGHT_ENEMY_aire 
        self.image = pygame.image.load(url_imagen)
        self.image = pygame.transform.scale(self.image, (self.enemigo_width, self.enemigo_height))
        self.forma = pygame.Rect(randint(0, WIDTH - self.enemigo_width), randint(-HEIGHT, -HEIGHT//2), self.enemigo_width, self.enemigo_height)
        self.speed = 3

    def update(self):
        self.forma.y += self.speed  # Mover el enemigo hacia abajo
        if self.forma.top > HEIGHT:
            self.reset()  # Reiniciar la posición si sale de la pantalla

    def reset(self):
        self.forma.y = -self.enemigo_height  # Posición inicial en Y
        self.forma.x = randint(0, WIDTH - self.enemigo_width)  # Posición aleatoria en X

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.forma)
        
class Enemigos_del_piso():
    def __init__(self, x, y,animaciones,velocidad_del_enemigo_piso):
        self.flip = False   
        self.animacion= animaciones 
        self.frame = 4
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame]
        self.forma = pygame.Rect(0, 0, WIDTH_ENEMY_PISO, HEIGHT_ENEMY_PISO)
        self.forma.center = (x, y)
        self.velocidad_x = velocidad_del_enemigo_piso

    def update(self):
        cooldown_animacion = 100
        self.image = self.animacion[self.frame]
        if pygame.time.get_ticks() - self.update_time >=cooldown_animacion:
            self.frame = self.frame + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame >= len(self.animacion):
            self.frame = 0
    def movimiento(self,WIDTH):

        nueva_x = self.forma.x + self.velocidad_x
        if nueva_x < 0 or nueva_x + WIDTH_PJ > WIDTH:
            self.velocidad_x = -self.velocidad_x 
            nueva_x = self.forma.x + self.velocidad_x  
        self.forma.x = nueva_x
        if self.velocidad_x < 0:
            self.flip = True
        if self.velocidad_x > 0:
            self.flip = False
        
    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        
    







