import pygame
import sys
from funciones import *
interfaz_de_volumen = pygame.display.set_mode((WIDTH, HEIGHT))
def pantalla_de_volumen():
    in_ejecution = True
    fondo_settings = poner_fondo("source\personaje.py\imagen_de_settings.jpeg")
    volumen = 50
    flag_boton_cliked = False
    while in_ejecution:
        interfaz_de_volumen.blit(fondo_settings, (0,0))  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                in_ejecution = False
        if dibujar_boton(interfaz_de_volumen,"subir volumen", pygame.Rect(570, 300, 200, 50), VIOLET, YELLOW,TRANSPARENCY):
            if not flag_boton_cliked and pygame.mouse.get_pressed()[0]:
                flag_boton_cliked = True
                volumen += 10
                modificar_volumen(volumen)

        if dibujar_boton(interfaz_de_volumen,"bajar volumen", pygame.Rect(570, 400, 200, 50), VIOLET, YELLOW,TRANSPARENCY):
           if not flag_boton_cliked and pygame.mouse.get_pressed()[0]:
                flag_boton_cliked = True
                volumen -= 10
                modificar_volumen(volumen)



            

        pygame.display.flip()
        pygame.display.set_caption("adventures of red slime")


def go__subir_bajar_volumen ():
    pantalla_de_volumen()