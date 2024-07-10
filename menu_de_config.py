import pygame
import sys
from constantes import *
from funciones import *
from configuracion_elegir_musica import*
from configuracion_De_subir_Y_bajar_volumen import*
cantidad_de_veces_clikeada = 0
opciones_screen = pygame.display.set_mode((WIDTH, HEIGHT))

def config_menu(SCREEn_de_opciones):
    clock = pygame.time.Clock()
    in_ejecution = True
    fondo_settings = poner_fondo("source\personaje.py\imagen_de_settings.jpeg")
    
    while in_ejecution:
        mouse_over_button = False
        SCREEn_de_opciones.blit(fondo_settings, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                in_ejecution = False
            
        if dibujar_boton(SCREEn_de_opciones,"select music", pygame.Rect(490, 300, 500, 50), VIOLET, YELLOW,TRANSPARENCY,mostrar_menu_de_eleccion_de_musica):
           pass
           
                
       
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
       
     
        

        # Dibujar elementos de configuración aquí

        pygame.display.flip()
        clock.tick(60)

def menu_de_configuraciones():
    config_menu(opciones_screen)

opciones_screen = pygame.display.set_mode((WIDTH, HEIGHT))
def config_loop():

   
    clock = pygame.time.Clock()
    in_ejecution = True
    fondiu = poner_fondo("source\personaje.py\imagen_de_settings.jpeg")
    while in_ejecution:
        flag_boton_cliked = False
        clock.tick(FPS)
        opciones_screen.blit(fondiu, (0,0))  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                in_ejecution = False
            
        if dibujar_boton(opciones_screen,"tema_1",pygame.Rect(570, 200, 300, 60), VIOLET, YELLOW,TRANSPARENCY):
            if not flag_boton_cliked and pygame.mouse.get_pressed()[0]:
                flag_boton_cliked = True
                x = cambio_de_url("tema_1")
                temon(x)
                
        if dibujar_boton(opciones_screen,"tema_2",pygame.Rect(570, 300, 300, 60), ORANGE, YELLOW,TRANSPARENCY):
            if not flag_boton_cliked and pygame.mouse.get_pressed()[0]:
                flag_boton_cliked = True
               
                x = cambio_de_url("tema_2")
                temon(x)
                export_json_file("url_de_tema_elegido.json",x)
                
        if dibujar_boton(opciones_screen,"tema_3",pygame.Rect(570, 400, 300, 50), WHITE, YELLOW,TRANSPARENCY):
            if not flag_boton_cliked and pygame.mouse.get_pressed()[0]:
                flag_boton_cliked = True
                mouse_over_boton = True
                x = cambio_de_url("tema_3")
                temon(x)
                export_json_file("url_de_tema_elegido.json",x)
                
            
        if dibujar_boton(opciones_screen,"tema_4",pygame.Rect(570, 500, 200, 50), GREEN, YELLOW,TRANSPARENCY):
            if not flag_boton_cliked and pygame.mouse.get_pressed()[0]:
                flag_boton_cliked = True
                mouse_over_boton = True
                x = cambio_de_url("tema_4")
                temon(x)
                export_json_file("url_de_tema_elegido.json",x)
        pygame.display.flip()
        pygame.display.set_caption("elegir musica")
        #esto dibuja un rectasngulo que no sabes para que sirve
        
    # Llamar a la pantalla de game over



def mostrar_menu_de_eleccion_de_musica():
  config_loop()


