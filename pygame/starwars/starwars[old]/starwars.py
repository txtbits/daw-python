# -*- coding: utf-8 -*-

''' Clon de Space Invaders
#   (Basado en un script original de Kevin Harris)
'''

import random
import os, pygame
from pygame.locals import *
from time import sleep

ANCHO  = 800
ALTO = 600


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
    (Nave del Jugador)
    '''
    
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.nave = os.path.join("data","xwing.bmp")
        self.image = cargarImagen( "xwing.bmp", True )
        self.explosion = os.path.join("data","explosion.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO/2,ALTO)
        self.dx = 0
        self.dy = 0
        self.puntos = 0
        self.vidas = 3

    def update( self ):
        self.rect.move_ip( (self.dx, self.dy) )

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO

        if self.rect.top <= ALTO/2:
            self.rect.top = ALTO/2
        elif self.rect.bottom >= ALTO:
            self.rect.bottom = ALTO


 
class TIEFighter( pygame.sprite.Sprite ):
    '''Sprite TIEFighter
    (Naves enemigas)
    '''
    
    def __init__( self, posx ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargarImagen( "tie_fighter.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = 120
        self.dx = random.randint( -5, 5 )
        self.dy = random.randint( -5, 5 )
        
    def update( self ):
        self.rect.move_ip( (self.dx, self.dy) )

        if self.rect.left < 0 or self.rect.right > ANCHO:
            self.dx = -(self.dx)

        if self.rect.top < 0 or self.rect.bottom > ALTO/2:
            self.dy = -(self.dy)

        disparar = random.randint( 1, 60 )
        if disparar == 1:
            tiefighterLaserGrupo.add( TIEFighterLaser( self.rect.midbottom ) )
            tiefighterDisparo.play()



class XWingLaser( pygame.sprite.Sprite ):
    '''Sprite XWingLaser
    (Disparos de jugador) 
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
    (Disparos del enemigo)
    '''
    
    def __init__( self, pos ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargarImagen( "empire_laser.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        
    def update( self ):
        if self.rect.bottom >= ALTO:
            self.kill()
        else:
            self.rect.move_ip( (0,4) )

'''
Cuerpo Principal del Juego
'''

random.seed()
pygame.init()
visor = pygame.display.set_mode( (ANCHO, ALTO) )
pygame.display.set_caption( "Star Wars" )

fondo_imagen = cargarImagen( "background.bmp" )
visor.blit(fondo_imagen, (0,0))

explotar = cargarSonido( "explode1.wav" )
tiefighterDisparo = cargarSonido( "empire_laser.wav" )
xwingDisparo = cargarSonido( "rebel_laser.wav" )

xwing = XWing()
xwingGrupo = pygame.sprite.RenderUpdates(xwing)
xwingLaserGrupo = pygame.sprite.RenderUpdates()
tiefighterGrupo = pygame.sprite.RenderUpdates()
tiefighterGrupo.add( TIEFighter( 150 ) )
tiefighterGrupo.add( TIEFighter( 400 ) )
tiefighterGrupo.add( TIEFighter( 650 ) )
tiefighterLaserGrupo = pygame.sprite.RenderUpdates()

jugando = True
intervaloEnemigos = 0
reloj = pygame.time.Clock()
iniciando = False
contador = 0

while jugando:
    reloj.tick( 60 )
    if iniciando:
        contador -= 1
        if contador == 0:
            iniciando = False
    for event in pygame.event.get():
        if event.type == QUIT:
            jugando = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                jugando = False
            if event.key == K_SPACE:
                xwingLaserGrupo.add( XWingLaser( xwing.rect.midtop ) )
                xwingDisparo.play()
        elif event.type == KEYUP:
            xwing.dx , xwing.dy = 0 , 0
    
    teclasPulsadas = pygame.key.get_pressed()
    if teclasPulsadas[K_LEFT]:
        xwing.dx = -4
    if teclasPulsadas[K_RIGHT]:
        xwing.dx = 4
    if teclasPulsadas[K_UP]:
        xwing.dy = -4
    if teclasPulsadas[K_DOWN]:
        xwing.dy = 4

    intervaloEnemigos += 1
    if intervaloEnemigos >= 200:
        tiefighterGrupo.add( TIEFighter( 320 ) )
        intervaloEnemigos = 0

    xwingGrupo.update()
    xwingLaserGrupo.update()
    tiefighterGrupo.update()
    tiefighterLaserGrupo.update()

    for pum in pygame.sprite.groupcollide( tiefighterGrupo, xwingLaserGrupo, 1, 1):
        explotar.play()
        xwing.puntos += 1
    
    if pygame.sprite.spritecollideany(xwing, tiefighterLaserGrupo):
        xwing.vidas -= 1
        xwing.rect.center = (ANCHO/2,ALTO)
        for nave in tiefighterGrupo:
            tiefighterGrupo.remove(nave)
        for disparo in tiefighterLaserGrupo:
            tiefighterLaserGrupo.remove(disparo)
        for disparo in xwingLaserGrupo:
            xwingLaserGrupo.remove(disparo)
        iniciando = True
        contador = 2* 60

    tiefighterLaserGrupo.clear( visor, fondo_imagen )
    tiefighterGrupo.clear( visor, fondo_imagen )
    xwingLaserGrupo.clear( visor, fondo_imagen)
    xwingGrupo.clear( visor, fondo_imagen )
    
    if not iniciando:
        tiefighterLaserGrupo.draw( visor )
        xwingLaserGrupo.draw( visor )
        tiefighterGrupo.draw( visor )
    xwingGrupo.draw( visor )

    pygame.display.update()