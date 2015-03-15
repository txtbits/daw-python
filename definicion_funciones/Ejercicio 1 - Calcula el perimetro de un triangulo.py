# -*- coding: cp1252 -*-
from graphics import *
import math

import random

pantalla = GraphWin('Triángulos', 500, 300)

colores = ['red', 'blue', 'orange', 'yellow', 'pink', 'brown', 'black', 'green', 'grey', 'purple']


def cuadrado(cateto):
    return cateto * cateto

def distancia(punto1, punto2):
    dist = math.sqrt(cuadrado(punto2.x - punto1.x ) + cuadrado(punto2.y - punto1.y))
    return dist

p1 = pantalla.getMouse()
p1.draw(pantalla)
p2 = pantalla.getMouse()
p2.draw(pantalla)
p3 = pantalla.getMouse()
p3.draw(pantalla)
t = Polygon(p1, p2, p3)
t.draw(pantalla)
random_color = random.randint(0,9)
t.setFill(colores[random_color])


dist1_2 = distancia(p1,p2)
dist2_3 = distancia(p2,p3)
dist3_1 = distancia(p3,p1)

perimetro = dist1_2 + dist2_3 + dist3_1
t = Text(Point(200,200), perimetro)
t.draw(pantalla)

pantalla.getMouse()








