# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from gamelib import *
import sys
from time import sleep

pygame.init()

# Definiciones ...
fps = 60

# Creación de objetos
pelota = Pelota()
raqueta1 = Raqueta(50)
raqueta2 = Raqueta(740)
reloj = pygame.time.Clock()

# Pantalla
visor = pygame.display.set_mode((800,600),FULLSCREEN)
sleep(2)
while True:
    #----------------------------------------------------------------#
    # Gestionar la velocidad del juego
    #----------------------------------------------------------------#
    reloj.tick(60)
    #----------------------------------------------------------------#
    # Bucle de eventos: Mirar si se quiere terminar el juego
    #----------------------------------------------------------------#
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
           
    # Updates ...
    pelota.update(raqueta1, raqueta2)
    teclasPulsadas = pygame.key.get_pressed()
    raqueta1.update_i(teclasPulsadas)
    raqueta2.update_d(teclasPulsadas)
    # Que juegue la máquina
    #raqueta2.update_auto(pelota)
    # Draw ...
    # Primero borra la pantalla en negro
    visor.fill(NEGRO)
    pelota.draw(visor)
    raqueta1.draw(visor)
    raqueta2.draw(visor)
    pygame.display.update()