# -*- coding: utf-8 -*-


# pedir numero

numero = int(raw_input('Introduce un número: '))

# suposición inicial
es_primo = True
for n in range(2,numero):
    if numero % n == 0:
        es_primo = False
        break # para el bucle

if es_primo:
    print numero, 'es primo'
else:
    print numero, 'no es primo'
