from graphics import *

pantalla = GraphWin('Coche', 400, 400)

puntos = []

for x in range(10):
    p = pantalla.getMouse()
    p.draw(pantalla)
    puntos.append(p)
    '''
    Es lo mismo que:
    puntos.append(pantalla.getMouse())
    '''

poligono = Polygon(puntos)
poligono.draw(pantalla)
pol.setFill('red')

pantalla.getMouse()
