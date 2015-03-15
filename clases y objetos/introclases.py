# -*- coding: utf-8 -*-

from graphics import GraphWin, Rectangle, Point, Text
from time import sleep

class Rectangulo_centro(object):
    # Definición de un rectángulo que se coloca en el centro de la pantalla
    def __init__(self, ventana):
        ancho = ventana.width/2
        alto = ventana.height/2
        p1 = Point(ancho - 20, alto - 10)
        p2 = Point(ancho + 20, alto + 10)
        self.r = Rectangle(p1, p2)
        self.r.draw(ventana)
        self.r.setFill('red')
    def color(self, c):
        # Pone el rectángulo del color 'c'
        self.r .setFill(c)
        
class Boton(object):
    def __init__(self, ventana, centro, ancho, alto, etiqueta):
        # Crea un botón en 'ventana', centrado el punto 'centro' de tamaño 'ancho' y 'alto' y con la etiqueta centrada
        # calculo de la posicion
        x, y = centro.getX(), centro.getY()
        w, h = ancho/2, alto/2
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        # rect del boton
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        # dibuja el boton en pantalla y le pone color
        self.rect = Rectangle(p1, p2)
        self.rect.draw(ventana)
        self.rect.setFill('lightgrey')
        # etiqueta (texto dentro del boton)
        self.etiqueta = Text(centro, etiqueta)
        self.etiqueta.draw(ventana)
        self.activar()
    def pulsado(self,p):
        # devuelve True si el punto p está dentro del botón. False en caso contrario.
        px = p.getX()
        py = p.getY()
        if px > self.xmin and px < self.xmax and py > self.ymin and py < self.ymax:
            return True
        else:
            return False
        
    def activar(self):
        self.etiqueta.setTextColor('black')
        self.activo = True
    def desactivar(self):
        self.etiqueta.setTextColor('grey')
        self.activo = False
        

# Generamos la ventana. Por defecto de 200x200.

w = GraphWin("Ejemplos con clases", 400, 200)

b1 = Boton(w, Point(100,100), 80, 40, 'Hola')
b2 = Boton(w, Point(300,100), 80, 40, 'Adiós')
while True:
    p = w.getMouse()
    if b1.pulsado(p):
        break
    if b2.pulsado(p):
        if b2.activo:
            b2.desactivar()
        else:
            b2.activar()
'''
mirect = Rectangulo_centro(w)
sleep(1)
mirect.color('green')
sleep(1)
mirect.color('blue')
sleep(1)
mirect.color('yellow')
'''

#w.getMouse() # Para que no se cierre el programa