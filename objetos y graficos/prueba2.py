from graphics import *
import random
g = GraphWin('Ejemplo graphics', 300, 200)
colores = ['red', 'black', 'blue', 'green', 'pink']
random.shuffle(colores)

for x in range(10):
    p = g.getMouse()
    tam = random.randint(10, 50)
    c = Circle(p,tam)
    c.draw(g)
    posicion = random.randint(0, 4)
    #c.setFill(colores.pop())
    c.setFill(colores[posicion])

# espera para no cerrar pantalla
g.getMouse()




'''
p = Point(150, 100)
p.draw(g)
p_1 = Point(10, 10)
p_1.draw(g)
p_2 = Point(290, 190)
p_2.draw(g)
r = Rectangle(p_1, p_2)
r.draw(g)
r.setFill('brown')
r.setOutline('orange')
r2 = Rectangle(Point(20,20), Point(280,180))
r2.draw(g)
r2.setFill('blue')
r2.setOutline('white')
c = Circle(p, 20)
c.draw(g)
c.setFill('black')
c.setOutline('yellow')

for x in range(100, 9, -10):
    c = Circle(p, x)
    c.draw(g)
'''
