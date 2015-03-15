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

# Desplazamiento de la pelota
pelotaDX = 5
pelotaDY = 5

# Inicialización posición raqueta
raquetaX = 50
raquetaY = 250

# Control pelota / velocidad
fps = 60
tiempo = 0


# Creación de la pantalla en modo FULLSCREEN
visor = pygame.display.set_mode((800,600),FULLSCREEN)

# Bucle principal
while True:
    # Control tiempo
    if pygame.time.get_ticks()-tiempo < 1000/fps:
        continue
    tiempo = pygame.time.get_ticks()

    
    # Eventos
    for evento in pygame.event.get():
        # Salir
        if evento.type == KEYDOWN and evento.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    # Updates
    if pelotaX < 5 or pelotaX > 795:
        pelotaDX = -pelotaDX
    if pelotaY < 5 or pelotaY > 595:
        pelotaDY = -pelotaDY
    pelotaX += pelotaDX
    pelotaY += pelotaDY


    # Draw
    visor.fill(NEGRO)
    pygame.draw.circle(visor, BLANCO, (pelotaX,pelotaY),4,0)
    pygame.draw.rect(visor, BLANCO, (raquetaX,raquetaY,10,50))
    pygame.display.update()
