# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# mario01.py
# Implemetación de sprites
#-----------------------------------------------------------------------
import sys
import pygame
from pygame.locals import *
import os
from random import randint
# Clase MiSprite
class MiSprite( pygame.sprite.Sprite ):
    # Inicializador de la clase
    def __init__( self, dibujo, posX, posY ):
        # Importante: Primero hay que inicializar la clase Sprite original
        pygame.sprite.Sprite.__init__( self )
        
        # Almacenar en el sprite la imagen deseada
        self.image = pygame.image.load(dibujo)
        self.image = self.image.convert()
        self.image.set_colorkey((255,255,255))
        
        # Definir el rect del sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (posX, posY)
        
        # Definir las velocidad
        self.dx = 1 
        self.dy = 1

        
    # Mover
    def update(self):
        # Modificar la posición del sprite
        self.rect.move_ip(self.dx,self.dy)
        # Comprobar si hay que cambiar el movimiento
        if self.rect.left < 0 or self.rect.right > 640:
            self.dx = -self.dx
            self.girar()
            self.rect.move_ip(self.dx,self.dy)
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.dy = -self.dy
            self.rect.move_ip(self.dx,self.dy)
        # Simular la gravedad sumando una cantidad a la velocidad vertical
        self.dy = self.dy + 0.5
    
    def girar(self):
        self.image = pygame.transform.flip( self.image, True, False )

        
# Inicializar PyGame y crear la Surface del juego
pygame.init()
visor = pygame.display.set_mode((640, 480))



# Inicializar el sprite
ruta = os.path.join("data","mario.bmp")
sprite = MiSprite(ruta, randint(0,200), randint(40,280))
grupo = pygame.sprite.RenderUpdates( sprite )
sprite2 = MiSprite(ruta, randint(201,500), randint(40,290))
grupo2 = pygame.sprite.RenderUpdates( sprite2 )

# Crear un reloj para controlar la animación
reloj = pygame.time.Clock()

# El bucle de la animación
while 1:
    #Fijar la animación a 60 fps
    reloj.tick(60)
    
    # Gestionar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        #Mira si se ha apretado el ratón
        elif evento.type == MOUSEBUTTONDOWN:
            # guarda la posición del clic en 2 variables
            posx, posy = evento.pos
            raton = pygame.Rect(posx, posy, 5, 5)
            for mario in grupo2:
                if mario.rect.collidepoint(posx,posy):
                    grupo2.remove(mario)
                else: 
                    spriteraton = MiSprite(ruta, posx-51, posy)
                    grupo2.add(spriteraton)
                    
    # Mira si hay alguna colisión:
    if pygame.sprite.spritecollideany(sprite, grupo2):
        sprite.dx = -sprite.dx
        sprite.dy = -sprite.dy
        sprite2.dx = -sprite2.dx
        sprite2.dy = -sprite2.dy
        sprite.girar()
        sprite2.girar()


    
    # Actualizar el sprite
    grupo.update()
    grupo2.update()

    # Dibujar la escena
    visor.fill((255,255,255))
    grupo.draw( visor )
    grupo2.draw( visor )

    # Mostrar la animación
    pygame.display.update()
