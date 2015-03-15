# -*- coding: utf-8 -*-

import random
import os, pygame
from pygame.locals import *

def cargarImagen( archivo, usarTransparencia = False ):
    '''
    Función cargarImagen()
    ( Carga una imagen desde un archivo, devolviendo el objeto apropiado)
    
    '''
    
    lugar = os.path.join( "data", archivo )

    try:
        imagen = pygame.image.load( lugar )
    except pygame.error, mensaje:
        print "No puedo cargar la imagen:", lugar
        raise SystemExit, mensaje

    imagen = imagen.convert()

    if usarTransparencia:
        colorTransparente = imagen.get_at( (0,0) )
        imagen.set_colorkey( colorTransparente )

    return imagen



def cargarSonido( archivo ):
    '''
    ( Carga un sonido desde un archivo, devolviendo el objeto apropiado)
    '''
      
    class sinSonido:
        def play( self ):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return sinSonido()

    lugar = os.path.join( "data", archivo )

    try:
        sound = pygame.mixer.Sound( lugar )
    except pygame.error, message:
        print "No puedo cargar el sonido:", lugar
        raise SystemExit, message

    return sound



class XWing( pygame.sprite.Sprite ):
    '''Sprite XWing
    #   (Nave del Jugador)
    '''
    
    def __init__( self,screen ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargarImagen( "xwing.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.center = (screen.width/2,screen.height)
        self.dx = 0
        self.dy = 0

    def update( self,screen ):
        self.rect.move_ip( (self.dx, self.dy) )

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen.width:
            self.rect.right = screen.width

        if self.rect.top <= screen.height/2:
            self.rect.top = screen.height/2
        elif self.rect.bottom >= screen.height:
            self.rect.bottom = screen.height


 
class TIEFighter( pygame.sprite.Sprite ):
    
    '''Sprite TIEFighter
    #   (Naves enemigas)
    '''
    
    def __init__( self, posx ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargarImagen( "tie_fighter.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = 120
        self.dx = random.randint( -5, 5 )
        self.dy = random.randint( -5, 5 )
        
    def update( self, screen ):
        self.rect.move_ip( (self.dx, self.dy) )

        if self.rect.left < 0 or self.rect.right > screen.width:
            self.dx = -(self.dx)

        if self.rect.top < 0 or self.rect.bottom > screen.height/2:
            self.dy = -(self.dy)

        disparar = random.randint( 1, 60 )
        if disparar == 1:
            tiefighterLaserGrupo.add( TIEFighterLaser( self.rect.midbottom ) )
            tiefighterDisparo.play()



class XWingLaser( pygame.sprite.Sprite, screen ):
    
    '''Sprite XWingLaser
    #   (Disparos de jugador) 
    '''
        
    def __init__( self, pos ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargarImagen( "rebel_laser.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update( self ):
        if self.rect.bottom <= 0:
            self.kill()
        else:
            self.rect.move_ip( (0,-4) )
            


class TIEFighterLaser( pygame.sprite.Sprite ):
    '''Sprite TIEFighterLaser
    #   (Disparos del enemigo)
    '''
    
    def __init__( self, pos ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargarImagen( "empire_laser.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        
    def update( self ):
        if self.rect.bottom >= screen.height:
            self.kill()
        else:
            self.rect.move_ip( (0,4) )