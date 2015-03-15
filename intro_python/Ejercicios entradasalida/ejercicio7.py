#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
from math import sqrt

print 'Ejercicio 7'
print '-'*60

cateto1 = float(raw_input('Introduce cateto1: '))
cateto2 = float(raw_input('Introduce cateto2: '))

hipotenusa = sqrt ( (cateto1**2) + (cateto2**2))

print 'La hipotenusa es: ', hipotenusa


raw_input('Pulse la tecla enter para finalizar')
