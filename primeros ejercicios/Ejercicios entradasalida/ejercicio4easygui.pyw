# -*- coding: cp1252 -*-
#Calculen el per�metro y �rea de un c�rculo dado su radio.
from math import pi
import easygui

radio = easygui.enterbox('Elige el radio del c�rculo', '�rea y Per�metro del C�rculo', image='figcir.gif')
radio = float(radio)

area = pi * (radio**2)
perimetro = 2*pi*radio
easygui.msgbox('El �rea es %f \nEl perimetro es %f' % (area, perimetro), '�rea y Per�metro del C�rculo', image='figcir.gif')
