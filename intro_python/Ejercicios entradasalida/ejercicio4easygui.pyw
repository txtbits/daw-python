# -*- coding: cp1252 -*-
#Calculen el perímetro y área de un círculo dado su radio.
from math import pi
import easygui

radio = easygui.enterbox('Elige el radio del círculo', 'Área y Perímetro del Círculo', image='figcir.gif')
radio = float(radio)

area = pi * (radio**2)
perimetro = 2*pi*radio
easygui.msgbox('El área es %f \nEl perimetro es %f' % (area, perimetro), 'Área y Perímetro del Círculo', image='figcir.gif')
