#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este programa es sólo el comienzo de un ping-pong muy simple
pong02.py
'''

# Imports generales
import pygame
import sys
from pygame.locals import *

# Inicialización entorno
pygame.init()

# Definiciones de colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)

# Inicialización posición pelota
pelotaX = 50
pelotaY = 50


# Creación de la pantalla en modo FULLSCREEN
visor = pygame.display.set_mode((800,600)),FULLSCREEN)

# Bucle principal
while True:
    # Eventos
    for evento in pygame.event.get():
        # Salir
        if evento.type == KEYDOWN and evento.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    # Updates
    pelotaX += 5
    pelotaY += 5

    # Draw
    visor.fill(NEGRO)
    pygame.draw.circle(visor, BLANCO, (pelotaX,pelotaY),4,0)
    pygame.display.update()
