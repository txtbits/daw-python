#Calculen el volumen de una esfera dado su radio.
from math import pi
import easygui

print 'Ejercicio 5'
print '-'*60

radio = easygui.enterbox('Introduce el radio','Volumen esfera')
radio = float(radio)
volumen = (4.0/3) * pi * (radio**3)

easygui.msgbox('El volumen de la esfera es: %f' % (volumen),'Volumen esfera')



