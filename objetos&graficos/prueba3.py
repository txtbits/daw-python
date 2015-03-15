# -*- coding: cp1252 -*-
from graphics import *
import random

g = GraphWin('Epiléptico', 1920,1080)

c  = Circle(Point(900, 500), 500)

c.draw(g)
for r in range(255):
    for g in range(255):
        for b in range(255):
            c.setFill(color_rgb(r, g, b))
