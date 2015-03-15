# -*- coding: utf-8 -*-
 
'''
Created on 10/01/2012
 
@author: lm  / @fsalamero
'''
import pygame
import sys
import time
from pygame.locals import *
#------------------------------------------------------------------#
# Inicialización de Pygame
#------------------------------------------------------------------#
#pygame.mixer.pre_init(44100,16,2,1024)
 
pygame.init()
#------------------------------------------------------------------#
# Definición de variables
#------------------------------------------------------------------#
fps = 60
tiempo = 0
BLANCO = (255,255,255)
AMARILLO = (255,255,0)
pelotaX = 50
pelotaY = 50
pelotaDX = 5
pelotaDY = 5
raquetaX = 50
raquetaY = 250
raquetaDY = 5
raqueta2X = 740
raqueta2Y = 250
raqueta2DY = 5
puntos1 = 0
puntos2 = 0
tipoLetra = pygame.font.Font('data/Grandezza.ttf', 96)
tipoLetra2 = pygame.font.Font('data/Grandezza.ttf', 24)
tipoLetra3 = pygame.font.Font('data/Grandezza.ttf', 48)
sonidoPelota = pygame.mixer.Sound('data/sonidoPelota.wav')
sonidoRaqueta = pygame.mixer.Sound('data/sonidoRaqueta.wav')
sonidoError = pygame.mixer.Sound('data/sonidoError.wav')
 
sonidoAplausos = pygame.mixer.Sound('data/sonidoAplausos.wav')
sonidoLaser = pygame.mixer.Sound('data/onidoLaser.wav')
imagenDeFondo = 'data/pingpong.jpg'
#------------------------------------------------------------------#
# Creación de la pantalla de juego (SURFACE)
#------------------------------------------------------------------#
visor = pygame.display.set_mode((800,600),FULLSCREEN)
#------------------------------------------------------------------#
# Funciones del programa
#------------------------------------------------------------------#
def pausa():
# Esta función hace que se espera hasta que se pulse una tecla
    esperar = True
    while esperar:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                    esperar = False
    sonidoLaser.play()
   
def mostrarIntro():
# Muestra la pantalla de inicio y espera
    fondo = pygame.image.load(imagenDeFondo).convert()
    visor.blit(fondo, (0,0))
    mensaje1 = 'PONG'
    texto1 = tipoLetra.render(mensaje1, True, AMARILLO)
    mensaje2 = 'Pulsa una tecla para comenzar'
    texto2 = tipoLetra2.render(mensaje2, True, BLANCO)
    visor.blit(texto1, (50,100,200,100))
    visor.blit(texto2, (235,340,350,30))
    pygame.display.update()
    pausa()
 
def dibujarJuego():
    # Dibuja la mesa, la pelota, las raquetas y los marcadores
    # Primero borra la pantalla en negro
    visor.fill((0,0,0))
    # Dibuja la pelota y las raquetas
    pygame.draw.circle(visor, BLANCO, (pelotaX,pelotaY),4,0)
    pygame.draw.rect(visor, BLANCO, (raquetaX,raquetaY,10,50))
    pygame.draw.rect(visor, BLANCO, (raqueta2X,raqueta2Y,10,50))
    # Dibuja la red
    for i in range(10):
        pygame.draw.rect(visor, BLANCO, (398,10+60*i,4,30))
    # Dibuja los marcadores
    marcador1 = tipoLetra.render(str(puntos1), True, BLANCO)
    marcador2 = tipoLetra.render(str(puntos2), True, BLANCO)
    visor.blit(marcador1, (300,20,50,50))
    visor.blit(marcador2, (450,20,50,50))
    # Y, finalmente, lo vuelca todo en pantalla
    pygame.display.update()
def decirGanador():
    # Decir qué jugador ha ganado y esperar
    sonidoAplausos.play()
    if puntos1 == 11:
        ganador = 'Jugador 1'
    else:
        ganador = 'Jugador 2'
    mensaje = 'Ganador: '+ ganador
    texto = tipoLetra3.render(mensaje, True, AMARILLO)
    visor.blit(texto, (110,350,600,100))
    pygame.display.update()
    pausa()
 
#------------------------------------------------------------------#
# Cuerpo principal del juego
#------------------------------------------------------------------#
 
pygame.mouse.set_visible(False)
mostrarIntro()
time.sleep(0.75)
while True:
    #----------------------------------------------------------------#
    # Gestionar la velocidad del juego
    #----------------------------------------------------------------#
    if pygame.time.get_ticks()-tiempo < 1000/fps:
        continue
    tiempo = pygame.time.get_ticks()
    #----------------------------------------------------------------#
    # Bucle de eventos: Mirar si se quiere terminar el juego
    #----------------------------------------------------------------#
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
           
    #----------------------------------------------------------------#
    # Mover la pelota
    #----------------------------------------------------------------#
    # Primero hay que vigilar por si hay que cambiar de dirección
    # Mira si se impacta con el jugador 1
    diff1 = pelotaY-raquetaY
    if pelotaX == raquetaX + 10 and diff1 >= 0 and diff1 <= 50:
        pelotaDX = -pelotaDX
        sonidoRaqueta.play()
    # Mira si se impacta con el jugador 2
    diff2 = pelotaY-raqueta2Y
    if pelotaX == raqueta2X and diff2 >= 0 and diff2 <= 50:
        pelotaDX = -pelotaDX
        sonidoRaqueta.play()
    # Mira si se ha llegado al borde de la pantalla
    if pelotaY < 5 or pelotaY > 595:
        pelotaDY = -pelotaDY
        sonidoPelota.play()
    # Mueve la pelota
    pelotaX += pelotaDX
    pelotaY += pelotaDY
    #----------------------------------------------------------------#
    # Mover las raquetas
    #----------------------------------------------------------------#
    # Mira si el jugador 1 mueve la raqueta
    teclasPulsadas = pygame.key.get_pressed()
    if teclasPulsadas[K_a]:
        raquetaY += raquetaDY
    if teclasPulsadas[K_q]:
        raquetaY -= raquetaDY
    # Vigilar que la raqueta no se salga de la pantalla
    if raquetaY < 0:
        raquetaY = 0
    elif raquetaY > 550:
        raquetaY = 550
    # Ahora hacemos lo mismo con el jugador 2
    if teclasPulsadas[K_l]:
        raqueta2Y += raqueta2DY
    if teclasPulsadas[K_p]:
        raqueta2Y -= raqueta2DY
    if raqueta2Y < 0:
        raqueta2Y = 0
    elif raqueta2Y > 550:
        raqueta2Y = 550
    #----------------------------------------------------------------#
    # Mirar si se ha ganado un punto
    #----------------------------------------------------------------#
    # Primero, mira si la pelota ha llegado al borde
    if pelotaX > 800 or pelotaX < 0:
    # En tal caso, recolocar juego y cambiar puntuación
        sonidoError.play()
        time.sleep(1)
        raquetaY = 250
        raqueta2Y = 250
        if pelotaX > 800:
            puntos1 = puntos1 + 1
        else:
            puntos2 = puntos2 + 1
        pelotaX = 400
        pelotaDX = -pelotaDX
    #----------------------------------------------------------------#
    # Dibujar el juego en pantalla
    #----------------------------------------------------------------#
    dibujarJuego()
    #---------------------------------------------------------------#
    # Comprobar si el juego se ha acabado
    #---------------------------------------------------------------#
    if puntos1 == 11 or puntos2 ==11:
        decirGanador()
        puntos1 = 0
        puntos2 = 0
        visor.fill((0,0,0))
        mostrarIntro()
 