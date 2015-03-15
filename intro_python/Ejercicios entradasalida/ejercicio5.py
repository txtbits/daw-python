#Calculen el volumen de una esfera dado su radio.
from math import pi

print 'Ejercicio 5'
print '-'*60

radio = float(raw_input('Elige el radio: '))

print 'El volumen de la esfera es: ', (4.0/3) * pi * (radio**3)


raw_input('Pulse la tecla enter para finalizar')
