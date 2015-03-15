# -*- coding: cp1252 -*-
from graphics import *

import random

pantalla = GraphWin('Triángulos', 500, 300)

colores = ['red', 'blue', 'orange', 'yellow', 'pink', 'brown', 'black', 'green', 'grey', 'purple']



for x in range (10):
    p = pantalla.getMouse()
    p.draw(pantalla)
    p2 = pantalla.getMouse()
    p2.draw(pantalla)
    p3 = pantalla.getMouse()
    p3.draw(pantalla)
    t = Polygon(p, p2, p3)
    t.draw(pantalla)
    random_color = random.randint(0,9)
    t.setFill(colores[random_color])
  
pantalla.getMouse()

