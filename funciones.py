import pygame
from constantes import * 
import  sys
from random import *
from csv import *
import csv

def escalar_imagen(imagen,escala):
    """cambia el tamaño de ujna imagen

    Args:
        imagen (_una ruta de  imagen_): _imagen a escalar_
        escala (_int_): _escala_
    """
    w = imagen.get_width()

    h = imagen.get_height()

    new_imagen = pygame.transform.scale(imagen,(w*escala,h*escala))
    return new_imagen


def quit_game():
    pygame.quit()
    sys.exit()
def detectar_colision(rect_1, rect_2)-> bool:
    if  punto_en_rectangulo(rect_1.topleft, rect_2) or \
        punto_en_rectangulo(rect_1.topright, rect_2) or \
        punto_en_rectangulo(rect_1.bottomleft, rect_2) or \
        punto_en_rectangulo(rect_1.bottomright, rect_2) or \
        punto_en_rectangulo(rect_2.topleft, rect_1) or \
        punto_en_rectangulo(rect_2.topright, rect_1) or \
        punto_en_rectangulo(rect_2.bottomleft, rect_1) or \
        punto_en_rectangulo(rect_2.bottomright, rect_1):
        return True
    else:
        return False
    
def  punto_en_rectangulo(punto,rect)-> bool:
    x , y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom



def quit_game():
    pygame.quit()
    sys.exit()


def configuraciones (screen):
    opciones = pygame.display.set_mode((WIDTH, HEIGHT))
    

def temon(url,bol):
    sonido_on = bol
    if sonido_on:
        pygame.mixer.music.load(url)
        pygame.mixer_music.play(-1)
    else:
        pygame.mixer.music.stop()
def modificar_volumen(volume):
    temon
    pygame.mixer.music.set_volume(volume) 


def sonido_de_daño():
    pygame.mixer.music.load("source\\sonidos\\failure-2-89169.mp3")
    pygame.mixer_music.play(1)


def poner_fondo(url) :
    background  = pygame.image.load(url).convert()

    return background  
def contador(bol):
    contador = 0
    if  bol == True:
        contador += 1
def saber_si_se_estan_tocando_los_cuadrados():
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        pygame.time.delay(200)

        return "x"
        
            

def dibujar_boton(screen,text, rect, color, color_si_se_toca, alpha, action=None,):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    se_esta_tocando = rect.collidepoint(mouse_pos)
     
    # Crear una superficie para el botón
    boton_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    if se_esta_tocando:
        boton_surface.fill((*color_si_se_toca, alpha))
        if click[0] == 1 and action:
            pygame.time.delay(200)
            action()  
           
    else:
        boton_surface.fill((*color, alpha))
    
    # Dibujar el botón en la pantall
    screen.blit(boton_surface, (rect.x, rect.y))
    
    # Renderizar el texto y dibujarlo en la pantalla
    fuente = font.render(text, True, WHITE)
    screen.blit(fuente, (rect.x + (rect.width - fuente.get_width()) // 2, rect.y + (rect.height - fuente.get_height()) // 2))
    return se_esta_tocando 


def elegir_temon(str:str):
    """tututututuututtututututuuttutututururututututturtrutrutrutrutrtrutrurtutrutrtutututututrurururrutututururtrutrutrutu

    Args:
        str:str
    """
    cantidad_de_veces_clikeada = 0
    if str == "x": 
        cantidad_de_veces_clikeada += 1
        if cantidad_de_veces_clikeada > 3:
            cantidad_de_veces_clikeada = 0
   
    lista_de_temones = ["source\sonidos\marsh-27860.mp3",
                        "source\sonidos\chill-drum-loop-6887.mp3",
                        "source\sonidos\musica_fondo.mp3",
                        "source\\sonidos\\flat-8-bit-gaming-music-instrumental-211547.mp3"
                                        ]
    temon(lista_de_temones[cantidad_de_veces_clikeada])
          


def cambio_de_url(tema_a_elegir):
    if tema_a_elegir ==  ("tema_1"):
        url = "source\\sonidos\\tema_1.mp3"
    elif tema_a_elegir == ("tema_2"):
        url = "source\\sonidos\\tema_2.mp3"
    elif tema_a_elegir == ("tema_3"):
        url = "source\\sonidos\\tema_3.mp3"
    elif  tema_a_elegir == ("tema_4"):
        url = "source\\sonidos\\tema_4.mp3"
    else:
        ValueError("no se ingreso una url")
    return url
    








def cargar_archivo_csv(nombre_archivo_data:str, lista):
    """summary

    Args:
        nombre_archivo_data (str): Nombre del archivo de donde se obtendra la informacion
    """
    try :
        with open(get_path_actual(nombre_archivo_data), "r", encoding="utf-8") as archivo:
            encabezado = archivo.readline().strip("\n").split(",")

            for linea in archivo.readlines():
                posts = {}
                linea = linea.strip("\n").split(",")
                id, user, likes, dislikes, followers = linea
                posts["id"] = int(id)
                posts["user"] = user
                posts["likes"] =int(likes)
                posts["dislikes"] = int(dislikes)
                posts["followers"] = int(followers)

                lista.append(posts)
    except :
        raise ValueError("No existe un archivo con ese nombre")
def get_path_actual(nombre_archivo):
    """summary

    Args:
        nombre_archivo (type): Nombre del archivo actual

    Returns:
        type: la ubicacion del archivo en el que se trabaja
    """
    import os
    ubi = os.path.dirname(__file__)

    return os.path.join(ubi, nombre_archivo)

def import_json_file(archivo_datos:str):
    """summary

    Args:
        archivo_datos (str): nombre del archivo .json a importar
    """
    import json
    with open(get_path_actual(archivo_datos), "r", encoding="utf-8") as archivo:
        dato = json.load(archivo)
    return dato

def export_json_file(archivo_destino:str,algo):
    import json
    with open(get_path_actual(archivo_destino), "w", encoding="utf-8") as archivo:
        json.dump(algo, archivo, indent=2)





def crear_archivo_tipo(lista:list):
    """summary

    Args:
        lista (list): lista con datos para crear archivo
    """
    

    with open(get_path_actual(lista + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista)):
            l = ",".join(lista[i]) + "\n"

        for persona in lista:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)




def wait_user(tecla):
    continuar = True
    while continuar :
        #pone aca el menu de pausa
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    continuar = False


def escribir_texto(text, font, color, surface,x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def save_score(player_name, score):
    with open("./source/scores.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player_name, score])