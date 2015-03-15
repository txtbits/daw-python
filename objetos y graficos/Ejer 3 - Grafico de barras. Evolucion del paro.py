# -*- coding: utf-8 -*-
from graphics import *

pantalla = GraphWin('Evolución del paro', 500, 300)

pantalla.setCoords(0,0,1,1)

l1 = Line(Point(0.1,0.1),Point(0.9,0.1))
l1.draw(pantalla)

l2 = Line(Point(0.1,0.1),Point(0.1,0.9))
l2.draw(pantalla)

r1 = Rectangle(Point(0.15,0.1),Point(0.2,0.38))
r1.draw(pantalla)
r1.setFill('red')

r2 = Rectangle(Point(0.25,0.1),Point(0.30,0.36))
r2.draw(pantalla)
r2.setFill('yellow')

r3 = Rectangle(Point(0.35,0.1),Point(0.4,0.35))
r3.draw(pantalla)
r3.setFill('purple')

r4 = Rectangle(Point(0.45,0.1),Point(0.5,0.42))
r4.draw(pantalla)
r4.setFill('green')

r5 = Rectangle(Point(0.55,0.1),Point(0.6,0.52))
r5.draw(pantalla)
r5.setFill('pink')

r6 = Rectangle(Point(0.65,0.1),Point(0.7,0.56))
r6.draw(pantalla)
r6.setFill('orange')

r7 = Rectangle(Point(0.75,0.1),Point(0.8,0.6))
r7.draw(pantalla)
r7.setFill('blue')


t = Text(Point(0.15,0.94),'Porcentaje de paro')
t.draw(pantalla)

t2 = Text(Point(0.93,0.06),'Año')
t2.draw(pantalla)
pantalla.getMouse()


