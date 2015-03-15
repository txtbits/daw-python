from graphics import *

def dibuja_cara(centro, tam, ventana):
    # silueta
    cara = Circle(centro, tam)
    cara.draw(ventana)
    cara.setFill('White')
    # ojos
    dx = tam/3
    dy = tam/3
    xojoi = centro.x - dx
    xojod = centro.x + dx
    yojo = centro.y - dy
    tam_ojo = tam/6
    ojoi = Circle(Point(xojoi, yojo), tam_ojo)
    ojod = Circle(Point(xojod, yojo), tam_ojo)
    ojoi.draw(pantalla)
    ojod.draw(pantalla)
    # boca
    dy = tam - 70
    p1x = centro.x - dx
    p2x = centro.x + dx
    py = centro.y - dy
    boca = Line(Point(p1x, py), Point(p2x, py))
    boca.draw(pantalla)
    
pantalla = GraphWin('Cara', 400, 400)

dibuja_cara(Point(200, 200), 50, pantalla)
