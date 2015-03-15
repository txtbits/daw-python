#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este programa es sólo el comienzo de un ping-pong muy simple
pong01.py
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

# Creación de la pantalla en modo FULLSCREEN
visor = pygame.display.set_mode((800,600),FULLSCREEN)

# Bucle principal
while True:
    # Eventos
    for evento in pygame.event.get():
        # Salir
        if evento.type == KEYDOWN and evento.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    # Updates
    
    # Draw
    visor.fill(NEGRO)
    pygame.draw.circle(visor, BLANCO, (50,50),4,0)
    pygame.display.update()
