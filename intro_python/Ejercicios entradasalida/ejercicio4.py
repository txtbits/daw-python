#Calculen el per�metro y �rea de un c�rculo dado su radio.
from math import pi

print 'Ejercicio 4'
print '-'*60

radio = float(raw_input('Elige el radio: '))

print 'El area del circulo es: ', pi * (radio**2)
print 'El perimetro del circulo es: ', 2*pi*radio

raw_input('Pulse la tecla enter para finalizar')
