# -*- coding: cp1252 -*-
#Calculen el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1,x2,y1,y2.
from math import pi
import easygui

print 'Ejercicio 6'
print '-'*60

x1 = float(easygui.enterbox('Introduce x1', 'Área rectángulo', image='figrec.gif'))
x2 = float(easygui.enterbox('Introduce x2', 'Área rectángulo', image='figrec.gif'))
y1 = float(easygui.enterbox('Introduce y1', 'Área rectángulo', image='figrec.gif'))
y2 = float(easygui.enterbox('Introduce y2', 'Área rectángulo', image='figrec.gif'))

base= x2-x1
altura= y2-y1

area = base * altura

easygui.msgbox('El área es %f' % (area), 'Área rectángulo', image='figrec.gif')

