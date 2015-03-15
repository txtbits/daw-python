# -*- coding: utf-8 -*-
'''
Estadística letras. El programa pide la ruta de un fichero de texto. Lo lee y muestra la frecuencia de repetición de las letras,
ordenadas de más repetida a menos repetida. Sólo muestra repetición de las letras y no de los signos de puntuación, números, etc.
Unifica mayúsculas y minúsculas.
'''
import string

def abrir_fichero(namefile):
    f = open(namefile)
    return f

namefile = raw_input('Introduce el nombre del fichero que quieres abrir: ')
f = abrir_fichero(namefile)
contenido = f.read()

for signo in string.punctuation:
    contenido = contenido.replace(signo, ' ')


palabras = contenido.split()

frecuencia = {}
for pal in palabras:
    frecuencia[pal] = frecuencia.get(pal, 0) + 1

for k in frecuencia:
    print k, frecuencia[k]
    
   
# ordenar resultado
import operator
ordenadas = sorted(frecuencia.items(), key=operator.itemgetter(1), reverse=True)

for k, v in ordenadas:
    print k, v