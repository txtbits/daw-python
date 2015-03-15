# -*- coding: utf-8 -*-
from graphics import *
from time import sleep

pantalla = GraphWin('Semáforo', 300, 600)
# pantalla.setBackground('black') para cambiar el color del fondo

r = Rectangle(Point(80,20), Point(220,300))
r.draw(pantalla)
r2 = Rectangle(Point(125,300),Point(175,550))
r2.draw(pantalla)
r.setFill('dark gray')
r2.setFill('black')

c = Circle(Point(150,65), 30)
c.draw(pantalla)
c.setFill('black')

c1 = Circle(Point(150,160), 30)
c1.draw(pantalla)
c1.setFill('black')

c2 = Circle(Point(150,255), 30)
c2.draw(pantalla)
c2.setFill('green')

for x in range(10):
    sleep(3)

    c2.setFill('black')
    c1.setFill('yellow')

    sleep(1.5)

    c1.setFill('black')
    c.setFill('red')
 
    sleep(3)
    
    c.setFill('black')
    c2.setFill('green')
