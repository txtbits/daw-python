#Calculen el perímetro y área de un círculo dado su radio.
from math import pi

print 'Ejercicio 4'
print '-'*60

radio = float(raw_input('Elige el radio: '))

print 'El area del circulo es: ', pi * (radio**2)
print 'El perimetro del circulo es: ', 2*pi*radio

raw_input('Pulse la tecla enter para finalizar')
