# -*- coding:utf-8 -*-


# imports iniciales
import pygame
from pygame.locals import *
from personajes_juego import Mono, Banana
import sys
import time
import os
from random import randint

pygame.init()

ANCHO, ALTO = 640, 480

pantalla = pygame.display.set_mode((ANCHO, ALTO)) # Entre dobles parentesis puesto que set_mode solo admite un único valor
pygame.display.set_caption('Jueguecillo pygame')

# Cargar recursos
ruta_fondo = os.path.join('sources','selva.png')
fondo = pygame.image.load(ruta_fondo)
fuente = pygame.font.Font(None, 28)

mono = Mono()


bananas = []
contador_bananas = 0
clock = pygame.time.Clock()
jugando = True
while jugando:
    clock.tick(150) # 30 veces por segundo
    # eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            jugando = False
 
    if randint(1,30) == 1:
        bananas.append(Banana())
    # mover, comprobar ...
    mono.mover()

    
    for banana in bananas:
        if mono.comer(banana):
            bananas.remove(banana)
            contador_bananas += 1
        else:
            banana.mover()
            banana.update()

 
    texto = fuente.render("Bananas: %3d" %contador_bananas, True, (255, 255, 255))
    
    # pintar
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(mono.imagen, mono.rect)
    for banana in bananas:
        pantalla.blit(banana.imagen, banana.rect)
    
    pantalla.blit(texto, [20,20])
    pygame.display.flip()
    
sys.exit()