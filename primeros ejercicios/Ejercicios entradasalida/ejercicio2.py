# Escribir un programa que pregunte al usuario dos números y luego muestre la suma, el producto y la media de los dos números
numero = raw_input('Elige un numero ')
numero2 = raw_input('Elige otro numero ')
numero = int(numero)
numero2 = int(numero2)
print 'La suma de los numeros es: ', numero + numero2
print 'El producto de los numeros es: ', numero * numero2
print 'La media de los numeros es: ', (numero+numero2)/2.
raw_input('Pulse la tecla enter para finalizar')
