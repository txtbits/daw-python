# -*- coding: utf-8 -*-

import string

fichero = raw_input('Intro ruta del fichero de texto a analizar: ')
 
# leemos el fichero como una cadena
texto = open(fichero).read()
 
# conversión a minúsculas
texto = texto.lower()

# reemplazo de signos de puntuacion por espacios
for signo in string.punctuation:
    texto.replace(signo, ' ')

# troceamos por palabras (por los espacios en blanco)
palabras = texto.split()  # palabras es ahora una lista de cadenas

frecuencia = {}
# contamos palabras. Incrementamos
for pal in palabras:
    frecuencia[pal] = frecuencia.get(pal, 0) + 1

# ordenar resultado
import operator
ordenadas = sorted(frecuencia.items(), key=operator.itemgetter(1), reverse=True)


# mostrar resultado
for clave, valor in ordenadas: # .items() te devuelve la palabra y el valor del diccionario.
    print clave, valor
