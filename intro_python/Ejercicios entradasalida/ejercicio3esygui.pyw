# -*- coding: cp1252 -*-
#Calculen el per�metro y �rea de un rect�ngulo dada su base y su altura.

import easygui

base = easygui.enterbox('Elige la base del rectangulo', '�rea rect�ngulo', image='figrec.gif')
altura = easygui.enterbox('Elige la altura del rectangulo', '�rea rect�ngulo', image='figrec.gif')
base = int(base)
altura = int(altura)

area = base * altura
perimetro = 2*base + 2*altura


easygui.msgbox('El �rea es %d \nEl perimetro es %d' % (area, perimetro), '�rea rect�ngulo', image='figrec.gif')
