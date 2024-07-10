import pygame
import sys
from funciones import *

def death_screen(screen, score):
    clock = pygame.time.Clock()
    running = True

    fondo = poner_fondo("source\personaje.py\game_over.jpeg")
    name = input("Enter your initials: ")
    with open('scores.txt', 'a') as file:
        file.write(f'{name} {score}\n')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                
        screen.blit(fondo, (0, 0))
        font = pygame.font.Font(None, 74)
        texto_de_muerte = font.render('Game Over', True, (255, 0, 0))
        puntaje = font.render(f'Score: {score}', True, (0, 0, 0))
        prompt_text = font.render('Press escape_para_salir', True, (0, 0, 0))
        
        screen.blit(texto_de_muerte, (screen.get_width() // 2 - texto_de_muerte.get_width() // 2, 200))
        screen.blit(puntaje, (screen.get_width() // 2 - puntaje.get_width() // 2, 300))
        screen.blit(prompt_text, (screen.get_width() // 2 - prompt_text.get_width() // 2, 400))

        pygame.display.flip()
        clock.tick(60)

def go_to_death():
    death_screen()
