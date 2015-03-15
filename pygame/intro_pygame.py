# -*- coding:utf-8 -*-


# imports iniciales
import pygame
from pygame.locals import *
from personajes import Mono, Nave, Banana
import sys
import time
import os

pygame.init()

ANCHO, ALTO = 640, 480

pantalla = pygame.display.set_mode((ANCHO, ALTO)) # Entre dobles parentesis puesto que set_mode solo admite un único valor
pygame.display.set_caption('Jueguecillo pygame')

# Cargar recursos
ruta_fondo = os.path.join('sources','selva.png')
fondo = pygame.image.load(ruta_fondo)
fuente = pygame.font.Font(None, 28)

mono = Mono()
nave = Nave()
bananas = []
for x in range(5):
    bananas.append(Banana())
jugando = True
while jugando:
    # eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            jugando = False
    
    # mover, comprobar ...
    mono.mover()
    nave.mover()
    for banana in bananas: 
        banana.mover()
    texto = fuente.render("Contador: %3d" %mono.rebotes, True, (255, 255, 255))
    
    # pintar
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(mono.imagen, (mono.rect))
    pantalla.blit(nave.imagen, (nave.rect))
    for banana in bananas:
        pantalla.blit(banana.imagen, (banana.rect))
    pantalla.blit(texto, [20,20])
    pygame.display.flip()
    
sys.exit()