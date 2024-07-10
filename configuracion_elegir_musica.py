import pygame
import sys
from constantes import *
from funciones import *



opciones_screen = pygame.display.set_mode((WIDTH, HEIGHT))
def config_loop(screen):
    mouse_over_boton = False
    clock = pygame.time.Clock()
    running = True
    fondiu = poner_fondo("source\personaje.py\imagen_de_settings.jpeg")
    while running:
        clock.tick(FPS)
        opciones_screen.blit(fondiu, (0,0))  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if dibujar_boton(opciones_screen,"tema_1",pygame.Rect(570, 200, 200, 50), VIOLET, YELLOW,TRANSPARENCY):
            mouse_over_boton = True
            
        if dibujar_boton(opciones_screen,"tema_2",pygame.Rect(570, 300, 200, 50), ORANGE, YELLOW,TRANSPARENCY):
            mouse_over_boton = True
        if dibujar_boton(opciones_screen,"tema_3",pygame.Rect(570, 400, 200, 50), WHITE, YELLOW,TRANSPARENCY):
            mouse_over_boton = True
        if dibujar_boton(opciones_screen,"tema_4",pygame.Rect(570, 500, 200, 50), GREEN, YELLOW,TRANSPARENCY):
            mouse_over_boton = True
        pygame.display.flip()
        pygame.display.set_caption("elegir musica")
        #esto dibuja un rectasngulo que no sabes para que sirve
        
    # Llamar a la pantalla de game over
  
def mostrar_menu_de_eleccion_de_musica():
  config_loop(opciones_screen)
