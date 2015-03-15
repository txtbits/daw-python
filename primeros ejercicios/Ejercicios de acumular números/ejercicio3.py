from easygui import *
'''
Escribe un programa que pida un número (el número de notas que vamos a introducir). Después pedirá las notas y calculará la media.
'''

# Etiqueta media inicializada a 0
total = 0
numnotas = int(enterbox('Introduce el número de notas: '))

# for ...range para recorrer el numero de notas
for num in range(numnotas):

    nota = int(enterbox('Introduce la nota nº %d : ' %(num+1)))
    
# Incrementando resultado en cada iteración
    total += nota 

# Mostrar resultado
media = total / float(numnotas)
msgbox('El resultado es %.2f' %media)
    
    
