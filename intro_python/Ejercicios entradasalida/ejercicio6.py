#Calculen el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1,x2,y1,y2.
from math import pi

print 'Ejercicio 6'
print '-'*60

x1 = float(raw_input('Introduce x1: '))
x2 = float(raw_input('Introduce x2: '))
y1 = float(raw_input('Introduce y1: '))
y2 = float(raw_input('Introduce y2: '))
base= x2-x1
altura= y2-y1


print 'El area del rectangulo es: ', base * altura


raw_input('Pulse la tecla enter para finalizar')
