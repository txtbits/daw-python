# -*- coding: cp1252 -*-
#Calculen el �rea de un rect�ngulo (alineado con los ejes x e y) dadas sus coordenadas x1,x2,y1,y2.
from math import pi
import easygui

print 'Ejercicio 6'
print '-'*60

x1 = float(easygui.enterbox('Introduce x1', '�rea rect�ngulo', image='figrec.gif'))
x2 = float(easygui.enterbox('Introduce x2', '�rea rect�ngulo', image='figrec.gif'))
y1 = float(easygui.enterbox('Introduce y1', '�rea rect�ngulo', image='figrec.gif'))
y2 = float(easygui.enterbox('Introduce y2', '�rea rect�ngulo', image='figrec.gif'))

base= x2-x1
altura= y2-y1

area = base * altura

easygui.msgbox('El �rea es %f' % (area), '�rea rect�ngulo', image='figrec.gif')

