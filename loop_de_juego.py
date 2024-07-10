import pygame
import sys
from clases import *
from constantes import * 
from funciones import*
from menu_de_config import *
from pantalla_de_muerte import *

pygame.init()
SCREEN_juego = pygame.display.set_mode((WIDTH,HEIGHT))

animaciones = []
for i in range (7):
    img = pygame.image.load(f"source\\personaje.py\\caminar({i}).png")
    img = escalar_imagen(img,escala_pj)
    animaciones.append(img)
animaciones_enemy_piso = []
for i in range (18):
    img = pygame.image.load(f"source\personaje.py\caminata_enemigo({i}).png")
    img = escalar_imagen(img,escala_enemigo)
    animaciones_enemy_piso.append(img)

pygame.display.set_caption("red slime adventures")
background  = pygame.image.load("source\personaje.py\level_3.png").convert()

def game_loop(screen):
    enemy_list = []
    cantidad_enemigos = 10
    meteoritos = Enemigos_voladores("source\personaje.py\misil_aeroespacial.png")
    for _ in range(cantidad_enemigos):
        nuevo_enemigo = Enemigos_voladores("source/personaje.py/misil_aeroespacial.png")
        enemy_list.append(nuevo_enemigo)

    jugador = Personaje(0,430,animaciones )
    enemigo_piso = Enemigos_del_piso(300,430,animaciones_enemy_piso,VELOICIDAD_ENEMY_PISO)
    clock = pygame.time.Clock()
    running = True
    contador_de_vidas = 3
    sonido_on = True
    temon(import_json_file("url_de_tema_elegido.json"),sonido_on)
    mover_izquierda = False
    mover_derecha = False
    jumping = False
    jump_speed = 20
    initial_jump_speed = jump_speed
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    inicio = pygame.time.get_ticks()
    coldow = False
    escudino = False
    count_son = 0
    cura_bandera = False
    pygame.draw.rect(SCREEN,BLUE, pygame.Rect((0,0),(WIDTH_PJ + 10, HEIGHT_PJ+10)),-1)
    dibujar_escudo =False
    contador_escudo = 0
    flag_boton_cliked = False
    ya_toco = True
   #BUCLEEEEE
    while running:

        vidas_texto = f"Tienes {contador_de_vidas} vidas"
        clock.tick(FPS)
        tiempo_actual = pygame.time.get_ticks() - inicio
        score = pygame.time.get_ticks() - inicio
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT,0)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                sonido_on = False
                escribir_texto("si desea continuar pulse p si no ",pygame.font.Font("source\Minercraftory.ttf",36),GREEN,SCREEN,200,500)
                wait_user(pygame.K_p)
                if dibujar_boton(SCREEN,"left game", pygame.Rect(570, 200, 200, 60), VIOLET, YELLOW,TRANSPARENCY):
                    break
                
                if  event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    continue
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_izquierda = True
                if event.key == pygame.K_d :
                    mover_derecha = True
                if event.key == pygame.K_SPACE and not jumping:
                    jumping = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mover_izquierda = False
                if event.key == pygame.K_d:
                    mover_derecha = False
                if event.key == pygame.K_SPACE and not jumping:
                    jumping = False
      
        delta_x = 0
        delta_y = 0
        if mover_derecha == True:
            delta_x = VELOICIDAD
        if mover_izquierda == True:
            delta_x -= VELOICIDAD
        #salto
        if jumping:
            delta_y -= jump_speed
            jump_speed -= GRAVITY
            if jump_speed < -initial_jump_speed:
                jumping = False
                jump_speed = initial_jump_speed


        SCREEN.blit(background, (0, 0))
        if dibujar_boton(SCREEN,"on/of sound", pygame.Rect(0,0, 400, 50), VIOLET, YELLOW,TRANSPARENCY,):
            if pygame.mouse.get_pressed()[0]:  # Verificar clic izquierdo del mouse
                if not flag_boton_cliked:
                    flag_boton_cliked = True
                    if sonido_on == False:
                        sonido_on = True
                    else:
                        sonido_on = False
            
                    # Llamar a temon con el estado actual de sonido_on
                    temon(import_json_file("url_de_tema_elegido.json"), sonido_on)

        else:
            flag_boton_cliked = False
    
                
        enemigo_piso.update()
        jugador.update()
        for meteoritos in enemy_list:
            meteoritos.update()
   
        contador_escudo += 1
        if not escudino == True:
                if detectar_colision(jugador.forma,enemigo_piso.forma) == True and ya_toco:
                    pygame.mixer.music.pause()
                    sonido_de_daño()
                    pygame.time.set_timer(pygame.USEREVENT,int(1000))
                    contador_escudo = -1
                    escudino = True
                    
        else:
            dibujar_escudo = True
            if dibujar_escudo == True:
                pygame.draw.rect(SCREEN,BLUE, jugador.forma,1)
                if contador_escudo ==  180 :
                    dibujar_escudo = False
                    contador_de_vidas -= 1
                    escudino = False
                     
        
       
        
        
        if contador_de_vidas == 3:
            escribir_texto(vidas_texto,pygame.font.Font("source\Minercraftory.ttf",36),GREEN,SCREEN,200,500)
        if contador_de_vidas == 2:
            escribir_texto(vidas_texto,pygame.font.Font("source\Minercraftory.ttf",36),GREEN,SCREEN,200,500)
        if contador_de_vidas == 1:
            escribir_texto(vidas_texto,pygame.font.Font("source\Minercraftory.ttf",36),GREEN,SCREEN,200,500)
        enemigo_piso.movimiento(1250)
        jugador.movimiento(delta_x,delta_y,1250,HEIGHT)
        enemigo_piso.dibujar(SCREEN)
        jugador.dibujar(SCREEN)
        escribir_texto(vidas_texto,pygame.font.Font("source\Minercraftory.ttf",36),GREEN,SCREEN,200,500)
        if tiempo_actual > 3000 and coldow == False:
            coldow == True
        if coldow == True:
               for meteoritos in enemy_list:
                meteoritos.dibujar(screen)
                meteoritos.update()
                tiempo_actual -= tiempo_actual

        # if tiempo_actual > 3000  or cura_bandera == False   :
        #     cura = pygame.draw.rect(SCREEN,BLUE,(pygame.Rect(100,450,40,40)),2)
        #     if detectar_colision(jugador.forma,cura):   
        #         contador_de_vidas += 1
        #         tiempo_actual = 0
        #         cura_bandera = True
            
        

        for meteorito in enemy_list:
            if not escudino == True:
                if detectar_colision(jugador.forma, meteorito.forma) and ya_toco:
                    pygame.mixer.music.pause()
                    sonido_de_daño()
                    pygame.time.set_timer(pygame.USEREVENT, int(1000))
                    contador_escudo = -1
                    escudino = True
                    break  # Para salir del bucle si se detecta una colisión
        for meteorito in enemy_list:
            meteorito.dibujar(screen)

        if escudino:
            dibujar_escudo = True
            pygame.draw.rect(SCREEN, BLUE, jugador.forma, 1)
            if contador_escudo == 180:
                contador_de_vidas -= 1
                dibujar_escudo = False
                escudino = False
                            
        score = score // 1000
        print(score)
        pygame.display.flip()
        pygame.display.set_caption("adventures of red slime")
        if contador_de_vidas <= 0:
            death_screen(screen_principal,score)
def mostrar_juego():
   game_loop(SCREEN_juego)

