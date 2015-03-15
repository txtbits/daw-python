#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este programa es sólo el comienzo de un ping-pong muy simple
pong02.py
'''

# Imports generales
import pygame
import sys
import time
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

# Inicialización posición y desplazamiento de la raqueta1
raquetaX = 50
raquetaY = 250
raquetaDY = 5

# Inicialización posición y desplazamiento de la raqueta2
raqueta2X = 740
raqueta2Y = 250
raqueta2DY = 5

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
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    diff1 = pelotaY-raquetaY
    if pelotaX == raquetaX + 10 and diff1 >=0 and diff1 <= 50:
        pelotaDX = -pelotaDX
    diff2 = pelotaY-raqueta2Y
    if pelotaX == raqueta2X and diff2 >= 0 and diff2 <= 50:
        pelotaDX = -pelotaDX

    # Updates
    if pelotaX < 5 or pelotaX > 795:
        pelotaDX = -pelotaDX
    if pelotaY < 5 or pelotaY > 595:
        pelotaDY = -pelotaDY
    pelotaX += pelotaDX
    pelotaY += pelotaDY

    teclasPulsadas = pygame.key.get_pressed()
    if teclasPulsadas[K_a]:
        raquetaY += raquetaDY
    if teclasPulsadas[K_q]:
        raquetaY -= raquetaDY
    
    if raquetaY < 0:
        raquetaY = 0
    elif raquetaY > 550:
        raquetaY = 550

    if teclasPulsadas[K_l]:
        raqueta2Y += raqueta2DY
    if teclasPulsadas[K_p]:
        raqueta2Y -= raqueta2DY
    if raqueta2Y < 0:
        raqueta2Y = 0
    elif raqueta2Y > 550:
        raqueta2Y = 550

    if pelotaX > 800 or pelotaX < 0:
        time.sleep(1)
        pelotaX = 400
        pelotaDX = -pelotaDX
        raquetaY = 250
        raqueta2Y = 250

    # Draw
    visor.fill(NEGRO)
    pygame.draw.circle(visor, BLANCO, (pelotaX,pelotaY),4,0)
    pygame.draw.rect(visor, BLANCO, (raquetaX,raquetaY,10,50))
    pygame.draw.rect(visor, BLANCO, (raqueta2X,raqueta2Y,10,50))
    pygame.display.update()
