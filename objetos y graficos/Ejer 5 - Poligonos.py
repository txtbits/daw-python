# -*- coding: cp1252 -*-
from graphics import *

import random

pantalla = GraphWin('Polígonos', 500, 300)

colores = ['red', 'blue', 'orange', 'yellow', 'pink', 'brown', 'black', 'green', 'grey', 'purple']


puntos = []
while True:
    p = pantalla.getMouse()
    p.draw(pantalla)
    puntos.append(p)
    objeto = Polygon(puntos)
    objeto.draw(pantalla)
    random_color = random.randint(0,9)
    objeto.setFill(colores[random_color])

''' Esta sin terminar'''

pantalla.getMouse()
