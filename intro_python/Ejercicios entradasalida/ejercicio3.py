#Calculen el perímetro y área de un rectángulo dada su base y su altura.

base = raw_input('Elige la base del rectangulo ')
altura = raw_input('Elige la altura del rectangulo ')
base = float(base)
altura = float(altura)
print 'El area del rectangulo es: ', base * altura
print 'El perimetro del rectangulo es: ', (base*2) + (altura*2)
raw_input('Pulse la tecla enter para finalizar')
