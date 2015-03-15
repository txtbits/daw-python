
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
    
    def iniciar(self):
        self.rect.centerx = 320
        self.rect.centery = 438
    
    def comer(self, banana):
        #Devuelve true cuando toca la banana
        return self.rect.colliderect(banana.rect)
    
    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.centerx += 4
        elif keys[K_LEFT]:
            self.rect.centerx -= 4
        if self.rect.right >= 640:
            self.rect.right = 639
        elif self.rect.left <= 0:
            self.rect.left = 1
    
class Banana(object):
    def __init__(self):
        ruta_banana = os.path.join('sources','banana.png')
        self.imagen = pygame.image.load(ruta_banana)
        self.rect = self.imagen.get_rect()
        # Para dividir la imagen en dos zonas:
        ancho = self.rect.width / 2
        self.rect.width = ancho
        self.sin_pelar = self.imagen.subsurface(self.rect) # self.imagen.subsurface(0, 0, self.rect.width, self.rect.height)
        self.pelada =  self.imagen.subsurface(ancho, 0, self.rect.width, self.rect.height)
        self.iniciar()
        self.imagen = self.sin_pelar
        self.contador = 0
        
    def update(self):
        self.contador += 1
        if self.contador >= 80:
            self.contador = 0
            if self.imagen == self.sin_pelar:
                self.imagen = self.pelada
            else:
                self.imagen = self.sin_pelar
        
    def iniciar(self):
        self.rect.centerx = randint(40,440)
        self.rect.centery = 1
        self.avance_y = 1
    
    def mover(self):
        self.rect.centery += 2