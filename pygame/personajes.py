
import pygame
from pygame.locals import *
import os
from random import randint

class Mono(object):
    def __init__(self):
        ruta_mono = os.path.join('sources','monkey.png')
        self.imagen = pygame.image.load(ruta_mono)
        self.rect = self.imagen.get_rect()
        self.iniciar()
        self.rebotes = 0
        
    def iniciar(self):
        # Iniciar x, y del mono
        self.rect.centerx = 320
        self.rect.centery = 240
        self.avance_x = 1
        self.avance_y = 1
        
    def mover(self):
        # mover, comprobar ...
        # Eje X
        if self.rect.right > 640:
            self.avance_x *= -1
            self.rect.right = 640
            self.rebotes += 1
        elif self.rect.left < 0:
            self.rect.left = 0
            self.avance_y *= -1
            self.rebotes += 1
        # Eje Y
        if self.rect.top < 0:
            self.rect.top = 0
            self.avance_y *= -1 
            self.rebotes += 1   
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.avance_y *= -1
            self.rebotes += 1
        # mover
        self.rect.centerx += self.avance_x
        self.rect.centery += self.avance_y
        
class Nave(object):
    def __init__(self):
        ruta_nave = os.path.join('sources','nave.png')
        self.imagen = pygame.image.load(ruta_nave)
        self.rect = self.imagen.get_rect()
        self.iniciar()
    
    def iniciar(self):
        self.rect.centerx = 320
        self.rect.centery = 450
    
    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.centerx += 2
        elif keys[K_LEFT]:
            self.rect.centerx -= 2
        if self.rect.right >= 640:
            self.rect.right = 639
        elif self.rect.left <= 0:
            self.rect.left = 1
    
class Banana(object):
    def __init__(self):
        ruta_banana = os.path.join('sources','banana.png')
        self.imagen = pygame.image.load(ruta_banana)
        self.rect = self.imagen.get_rect()
        self.iniciar()
        
    def iniciar(self):
        self.rect.centerx = randint(40,440)
        self.rect.centery = 1
        self.avance_y = 1
    
    def mover(self):
        if self.rect.top > 480:
            self.rect.bottom = 0
            self.avance_y *= 1
        self.rect.centery += self.avance_y