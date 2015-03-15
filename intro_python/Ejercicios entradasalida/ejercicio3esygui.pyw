# -*- coding: cp1252 -*-
#Calculen el perímetro y área de un rectángulo dada su base y su altura.

import easygui

base = easygui.enterbox('Elige la base del rectangulo', 'Área rectángulo', image='figrec.gif')
altura = easygui.enterbox('Elige la altura del rectangulo', 'Área rectángulo', image='figrec.gif')
base = int(base)
altura = int(altura)

area = base * altura
perimetro = 2*base + 2*altura


easygui.msgbox('El área es %d \nEl perimetro es %d' % (area, perimetro), 'Área rectángulo', image='figrec.gif')
