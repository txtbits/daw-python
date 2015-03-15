# -*- coding: utf-8 -*-
'''
Escribe una función según la siguiente especificación:
mover_a(forma, nuevo_centro)  --> mueve la forma a un nuevo punto.
forma es un objeto de graphics que tiene el método getCenter
nuevo_centro es un Point

'''
from graphics import *

ventana = GraphWin('Dibujar cara',300,300)

def mover_a(forma, nuevo_centro):
    c = Circle(nuevo_centro,30)
    c.draw(ventana)

nuevo_centro = int(raw_input('Elige donde quieres situar el objeto')
nuevo_centro = getMouse()

nuevo_centro.draw(pantalla)

mover_a(forma, nuevo_centro)

