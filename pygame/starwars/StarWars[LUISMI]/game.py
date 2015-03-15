# -*- coding: utf-8 -*-
'''
Clon de Space Invaders
(Basado en un script original de Kevin Harris)

A partir de un ejercicio de Fernando Salamero
'''

import pygame
from pygame.locals import *
from starwarslib import *
from random import randint

random.seed()

pygame.init()

visor = pygame.display.set_mode( (ANCHO, ALTO) )
pygame.display.set_caption( "Star Wars" )
pygame.mouse.set_visible(False)


fondo_intro = cargar_imagen( "intro.bmp")
fondo_jugando = cargar_imagen( "background.bmp" )
visor.blit(fondo_intro, (0,0))


xwing = XWing()
# grupo de Xwing para colisiones
xwingGrupo = pygame.sprite.RenderUpdates(xwing)
# grupod de naves enemigas
tiefighterGrupo = pygame.sprite.RenderUpdates()
# inicialización: tres naves
tiefighterGrupo.add( TIEFighter( 150 ) )
tiefighterGrupo.add( TIEFighter( 400 ) )
tiefighterGrupo.add( TIEFighter( 650 ) )


marcadorvidas = Marcador()
vida_perdida = False
iniciando = True    
jugando = False
cerrar = True
finalizando = False
contador = 0
intervaloEnemigos = 0
tipoLetra = pygame.font.SysFont('arial', 24)
tipoLetra2 = pygame.font.SysFont('arial', 17)


reloj = pygame.time.Clock()

while cerrar:
    reloj.tick( 60 )  # FPS
    
    if vida_perdida:
        contador -= 1
        if contador == 0:
            vida_perdida = False
            
    for event in pygame.event.get():
        if event.type == QUIT:
            cerrar = False
        elif event.type == KEYDOWN:   
            if event.key == K_SPACE:
                xwing.dispara()
                jugando = True
                iniciando = False
        elif event.type == KEYUP:
            xwing.dx , xwing.dy = 0 , 0
    
    teclasPulsadas = pygame.key.get_pressed()
    # Movimiento nave
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
        tiefighterGrupo.add( TIEFighter( randint(30,770) ) )
        intervaloEnemigos = 0
    
    # Actualiza
    xwingGrupo.update()
    XWing.laser_grupo.update()
    tiefighterGrupo.update()
    TIEFighter.laser_grupo.update()
    
    '''
    Elimina nuestra nave
    '''
    if pygame.sprite.spritecollideany(xwing, TIEFighter.laser_grupo):
        xwing.vidas -= 1
        xwing.rect.center = (ANCHO/2,ALTO)
        for nave in tiefighterGrupo:
            tiefighterGrupo.remove(nave)
        for disparo in TIEFighter.laser_grupo:
            TIEFighter.laser_grupo.remove(disparo)
        for disparo in XWing.laser_grupo:
            XWing.laser_grupo.remove(disparo)
        vida_perdida = True
        contador = 2* 60
    
    # Elimina enemigos tocados
    for pum in pygame.sprite.groupcollide(tiefighterGrupo, XWing.laser_grupo, 1, 1):
        pum.explota()
        xwing.puntos += 1
    
    pygame.sprite.groupcollide(TIEFighter.laser_grupo, XWing.laser_grupo, 1, 1)
    
    # fondo
    if iniciando:
    	visor.blit(fondo_intro, (0,0))
    elif jugando:
    	visor.blit(fondo_jugando, (0,0))
    '''
    elif finalizando:
    	visor.blit(fondo_fin, (0,0))
    '''

    # Borra
    TIEFighter.laser_grupo.clear( visor, fondo_jugando )
    tiefighterGrupo.clear( visor, fondo_jugando )
    XWing.laser_grupo.clear( visor, fondo_jugando)
    xwingGrupo.clear( visor, fondo_jugando )
    #Marcador.grupo.clear(visor,fondo_jugando)
    
    # Dibuja
    TIEFighter.laser_grupo.draw( visor )
    XWing.laser_grupo.draw( visor )
    tiefighterGrupo.draw( visor )
    xwingGrupo.draw( visor )
    if jugando:
        xwing.dibujar_puntos(visor,tipoLetra,tipoLetra2,xwing.puntos)
        marcadorvidas.dibuja(xwing.vidas,visor)
      
    
    # Actualiza
    pygame.display.update()
    
    
    