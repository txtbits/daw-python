# -*- coding: cp1252 -*-
'''Escribe un programa con graphics que vaya creando pelotas cada 3 segundos
(hasta 5). Las pelotas serán de colores y tamaños aleatorios
y se moverán por la pantalla rebotando en los lados.
Cuando hagas clic en una pelota, desaparecerá de la pantalla.
'''

from graphics import *
from random import randint
import time

pantalla = GraphWin("pelotas",400,400)

colores = "red green blue black yellow".split()

def crea_pelota(pantalla):
    '''Crea una pelota en la ventana pantalla.
    Devuelve la pelota
    '''
    r = randint(5,20)
    x = randint(10, pantalla.width-r)
    y = randint(10, pantalla.height-r)
    c = Circle(Point(x, y),r)
    c.setFill(colores[randint(0,4)])
    #velocidad = randint(2,8)
    c.dx = randint(2,15)
    c.dy = randint(2,15)
    c.draw(pantalla)
    return c


def mueve_pelota(p, pantalla):
    centro = p.getCenter()
    if p.dx >0:
        if p.radius + centro.x > pantalla.width:
            p.dx *= -1
    elif centro.x - p.radius < 0:
        p.dx *= -1
    if p.dy > 0:
        if p.radius + centro.y > pantalla.height:
            p.dy *=-1
    elif centro.y - p.radius < 0:
        p.dy *= -1 
    p.move(p.dx, p.dy)

pelotas = []
'''
for x in range(10):
    pelotas.append(crea_pelota(pantalla))
    time.sleep(0.1)
'''
antes = time.time()
while True:
    ahora = time.time()
    if ahora - antes > 2:
        pelotas.append(crea_pelota(pantalla))
        antes = ahora

    for p in pelotas:
        mueve_pelota(p, pantalla)
        time.sleep(0.01)

for p in pelotas
    p.undraw()


'''
checkmouse
def tocada(pelota, mouse):
'''
