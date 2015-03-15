# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os

# Constantes
BLANCO = (255,255,255)
AMARILLO = (255,255,0)
NEGRO = (0,0,0)


class Pelota(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.dx = 5
        self.dy = 5
        ruta_sonido = os.path.join('data','sonidoPelota.wav')
        self.sonido = pygame.mixer.Sound(ruta_sonido)

    def update(self, rizq, rder):
        # Mira si se ha llegado al borde de la pantalla
        if self.y < 5 or self.y > 595:
            self.dy *= -1
            self.sonido.play()
        '''
        if self.x < 5 or self.x > 795:
            self.dx *= -1
            self.sonido.play()
        '''
        # Mira si se impacta con el jugador 1
        diff1 = self.y - rizq.y
        if self.x == rizq.x + 10 and diff1 >= 0 and diff1 <= 50:
            self.dx *= -1
            rizq.sonido.play()
        # Mira si se impacta con el jugador 2
        diff2 = self.y-rder.y
        if self.x == rder.x and diff2 >= 0 and diff2 <= 50:
            self.dx *= -1
            rder.sonido.play()
        # Mueve la pelota
        self.x += self.dx
        self.y += self.dy
        self.ganar(rizq, rder)
        
    def ganar(self, rizq, rder):
        pierde = False
        if self.x <= 0:
            rder.puntos += 1
            pierde = True
        elif self.x >= 800:
            rizq.puntos += 1
            pierde = True
        if pierde == True:
            # sonido
            self.reiniciar()
            
    def reiniciar(self):
        self.x = 400
        self.y = 300
        self.dx *= -1
            
    def draw(self, screen):
        # Dibuja la pelota y las raquetas
        pygame.draw.circle(screen, BLANCO, (self.x,self.y),4,0)

class Raqueta(object):
    def __init__(self, posx):
        self.x = posx
        self.y = 250
        self.dy = 5
        self.puntos = 0
        ruta_sonido = os.path.join('data','sonidaRaqueta.wav')
        self.sonido = pygame.mixer.Sound(ruta_sonido)

    def update_i(self, teclas):
        '''teclas: teclas pulsadas'''
        # Mira si el jugador Izquierdo mueve la raqueta
        if teclas[K_a]:
            self.y += self.dy
        if teclas[K_q]:
            self.y -= self.dy
        self.corrige()
       
    def update_d(self, teclas):
        '''teclas: teclas pulsadas'''
        # Mira si el jugador Derecho mueve la raqueta
        if teclas[K_l]:
            self.y += self.dy
        if teclas[K_p]:
            self.y -= self.dy
        self.corrige()
        
    def corrige(self):
        # Vigilar que la raqueta no se salga de la pantalla
        if self.y < 0:
            self.y = 0
        elif self.y > 550:
            self.y = 550 
    
    def update_auto(self, pelota):
        self.y = pelota.y - 25
        self.corrige()
    
    def draw(self, screen):
        # Dibuja la pelota y las raquetas
        pygame.draw.rect(screen, BLANCO, (self.x,self.y,10,50))
        
'''
class Marcadores(self):
    def __init__ (self):
        
        
        # Dibuja la red
    for i in range(10):
        pygame.draw.rect(visor, BLANCO, (398,10+60*i,4,30))
    # Dibuja los marcadores
    marcador1 = tipoLetra.render(str(puntos1), True, BLANCO)
    marcador2 = tipoLetra.render(str(puntos2), True, BLANCO)
    visor.blit(marcador1, (300,20,50,50))
    visor.blit(marcador2, (450,20,50,50))'''