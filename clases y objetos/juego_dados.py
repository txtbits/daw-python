# -*- coding: utf-8 -*-
'''
Juego de dados:

- Crea una clase dado que permita crear dados gráficos con graphics
- Al crear un dado, le daremos la información de la ventana donde se pinta,
  el punto del centro del dado y su tamaño (en pixeles)
- El dado tendrá un método (ponValor(valor)) que asignará un valor numérico al dado y pintará
  los puntitos en la cara visible
'''

from graphics import *
from random import choice

class Boton(object):
    def __init__(self, v, centro, ancho, alto, etiqueta):
        '''Calculo de la posición del botón'''
        x, y = centro.getX(), centro.getY()
        w, h = ancho /2, alto /2
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        '''Creación del botón y etiqueta'''
        self.boton = Rectangle(p1, p2)
        self.boton.draw(v)
        self.boton.setFill('#CCC')
        self.etiqueta = Text(centro, etiqueta)
        self.etiqueta.setTextColor('#000')
        self.etiqueta.draw(v)
        self.desactivar()
        
    def pulsado(self, p):
        '''Comprobar si se pulsa el botón'''
        if p.getX() in range(self.xmin, self.xmax) and p.getY() in range(self.ymin, self.ymax):
            return True
        else:
            return False
        
    def activar(self):
        '''Activar estado'''
        self.estado = True
        
    def desactivar(self):
        '''Desactivar estado'''
        self.estado = False

class Dado(object):
    def __init__(self, v, centro, ancho, alto):
        '''Calculo de la posición del dado'''
        x, y = centro.getX(), centro.getY()
        w, h = ancho /2, alto /2
        self.ventana = v
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.dado = Rectangle(p1, p2)
        self.dado.draw(v)
        self.dado.setFill('#FFFFFF')
        '''Posiciones de las caras del dado'''
        self.pos1 = Point(self.xmin + w /2, self.ymin + h /2)
        self.pos2 = Point(self.xmin + w / 2, self.ymin + h)
        self.pos3 = Point(self.xmin + w / 2, self.ymin + h * 1.5)
        self.pos4 = Point(self.xmin + w, self.ymin + h)
        self.pos5 = Point(self.xmin + w * 1.5, self.ymin + h /2)
        self.pos6 = Point(self.xmin + w * 1.5, self.ymin + h)
        self.pos7 = Point(self.xmin + w * 1.5, self.ymin + h * 1.5)
        '''Pintar las caras del dado'''
        self.c1 = Circle(self.pos1, 4)
        self.c1.draw(self.ventana)
        self.c2 = Circle(self.pos2, 4)
        self.c2.draw(self.ventana)            
        self.c3 = Circle(self.pos3, 4)
        self.c3.draw(self.ventana)             
        self.c4 = Circle(self.pos4, 4)
        self.c4.draw(self.ventana)
        self.c5 = Circle(self.pos5, 4)
        self.c5.draw(self.ventana)
        self.c6 = Circle(self.pos6, 4)
        self.c6.draw(self.ventana)
        self.c7 = Circle(self.pos7, 4)
        self.c7.draw(self.ventana)
        
    def lanzarDado(self):
        '''Elegimos aleatoriamente una cara del dado asignada a un número'''
        posibilidades = [1, 2, 3, 4, 5, 6]
        num = choice(posibilidades)
        self.ponValor(num)
        return num
    
    def ponValor(self, valor=1):#
        '''Establecemos la cara del dado según valor'''
        self.limpiar()
        if valor == 1:
            self.c4.draw(self.ventana)
        elif valor == 2:
            self.c1.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 3:
            self.c1.draw(self.ventana)
            self.c4.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 4:
            self.c1.draw(self.ventana)
            self.c3.draw(self.ventana)
            self.c5.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 5:
            self.c1.draw(self.ventana)
            self.c3.draw(self.ventana)
            self.c4.draw(self.ventana)
            self.c5.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 6:
            self.c1.draw(self.ventana)
            self.c2.draw(self.ventana)
            self.c3.draw(self.ventana) 
            self.c5.draw(self.ventana)
            self.c6.draw(self.ventana)
            self.c7.draw(self.ventana)
        
    def limpiar(self):
        '''Limpiamos el dado antes de volver a pintar'''
        self.c1.undraw()
        self.c2.undraw()
        self.c3.undraw()
        self.c4.undraw()
        self.c5.undraw()
        self.c6.undraw()
        self.c7.undraw()   

'''Creamos la ventana'''
w = GraphWin('Juego de dados', 400, 400)

'''Creamos el marcador'''
etiqueta = Text(Point(300, 250), 'Puntos: 00')
etiqueta.draw(w)

'''Creamos los dados'''
d1 = Dado(w, Point(70, 120), 60, 60)
d1.ponValor()
d2 = Dado(w, Point(200, 120), 60, 60)
d2.ponValor()
d3 = Dado(w, Point(330, 120), 60, 60)
d3.ponValor()

'''Creamos los botones'''
b1 = Boton(w, Point(120, 250), 100, 40, 'Lanzar')
b1.activar()
b2 = Boton(w, Point(120, 320), 100, 40, 'Salir')
b2.activar()

'''Bucle principal de funcionamiento'''
while True:
    p = w.getMouse()
    if b1.pulsado(p):
        '''Si pulsamos el botón 1'''
        if b1.estado:
            num1 = d1.lanzarDado()
            num2 = d2.lanzarDado()
            num3 = d3.lanzarDado()
            numtotal = num1 + num2 + num3
            etiqueta.undraw()
            etiqueta = Text(Point(300, 250), 'Puntos: %.2d' % numtotal)
            etiqueta.draw(w)

    if b2.pulsado(p):
        '''Si pulsamos el botón 2'''
        if b2.estado:
            exit()
        
w.getMouse()