# -*- coding: utf-8 -*-
'''Escribe una función:
dibuja_cara(centro, tam, ventana) 
centro es un Point,
tam es un entero
ventana es un GraphWin donde se dibujará la cara
'''
from graphics import *

def dibujar_cara(centro,tam, ventana):
    c = Circle(centro,tam)
    c.draw(ventana)
    x = 150 -(tam/2)
    p1 = Point (x, x)

    c1 = Circle(p1, tam/8)
    c1.draw(ventana)

    y = 150 + (tam/2)
    p2 = Point(y,x)
    c2 = Circle(p2, tam/8)
    c2.draw(ventana)

    p3 = Point(150 - tam/3, 150 + tam/2)
    p4 = Point (150 + tam/3 , 150 + tam/2)

    l = Line(p3,p4)
    l.draw(ventana)

ventana = GraphWin('Dibujar cara',300,300)

tam = int(raw_input('Introduce el tamaño de la cara: '))

centro = Point(150,150)

dibujar_cara(centro, tam, ventana)


