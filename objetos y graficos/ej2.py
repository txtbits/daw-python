from graphics import *

pantalla = GraphWin('Coche', 1000, 300)

# Dibujamos el Sol
l = Point(40,40)
sol = Circle(l, 35)
sol.setFill('yellow')
sol.setOutline('yellow')
sol.draw(pantalla)

# Dibujamos Rayos del Sol
l1 = Line(Point(75,35),Point(125,25))
l1.setOutline('yellow')
l1.draw(pantalla)

l2 = Line(Point(70,60),Point(125,80))
l2.setOutline('yellow')
l2.draw(pantalla)

l3 = Line(Point(53,75),Point(70,120))
l3.setOutline('yellow')
l3.draw(pantalla)

l4 = Line(Point(25,70),Point(15,120))
l4.setOutline('yellow')
l4.draw(pantalla)

#---------------------------------

# Dibujamos el coche
r1 = Rectangle(Point(70,155), Point(130,180))
r1.setFill('dark grey')
r1.draw(pantalla)

r2 = Rectangle(Point(30,180), Point(170,210))
r2.setFill('red')
r2.draw(pantalla)

p = Point(45,210)
p2 = Point (155,210)

c1 = Circle(p, 10)
c1.setFill('black')
c1.draw(pantalla)

c2 = Circle(p2, 10)
c2.setFill('black')
c2.draw(pantalla)

'''
for pieza in r1, r2, c1, c2:
    pieza.draw(pantalla)
'''
#-------------------------------------

# Dibujamos la Carretera

carretera = Line(Point(0,221),Point(1000,221))
carretera.draw(pantalla)

#-------------------------------------


while (r1.p2.getX()) <= 940:
    for pieza in r1, r2, c1, c2:
        pieza.move(10, 0)
    time.sleep(0.2)
     

pantalla.getMouse()
