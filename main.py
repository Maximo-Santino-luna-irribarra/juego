import pygame
from constantes import * 
from clases import * 
from funciones import *
from loop_de_juego import *

pygame.init()

def main_menu():
    fondo_de_menu = poner_fondo("source\personaje.py\menu.jpg")
    screen_menu = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
       
        mouse_over_button = False
        screen_menu.blit(fondo_de_menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        if dibujar_boton(screen_menu,"play", pygame.Rect(570, 200, 200, 60), VIOLET, YELLOW,TRANSPARENCY,mostrar_juego):
            mouse_over_button = True
            
        if dibujar_boton(screen_menu,"settings", pygame.Rect(570, 300, 200, 50), VIOLET, YELLOW,TRANSPARENCY,menu_de_configuraciones):
            mouse_over_button = True
            
        if dibujar_boton(screen_menu,"score", pygame.Rect(570, 400, 200, 50), VIOLET, YELLOW,TRANSPARENCY,):
            mouse_over_button = True
           
        if dibujar_boton(screen_menu,"EXIT", pygame.Rect(570, 500, 200, 50), VIOLET, YELLOW,TRANSPARENCY, quit_game):
            mouse_over_button = True
           
        
        if mouse_over_button: 
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
       
        pygame.display.flip()
main_menu()
