# -*- coding: cp1252 -*-
'''
Pide a un usuario que escriba su nombre y su apellido.
T� lo mostrar�s correctamente: El nombre con las iniciales el may�sculas
y el apellido todo en may�sculas, aunque el usuario no lo haya escrito as�.
'''

nombre = raw_input('Introduce un nombre: ')
apellido = raw_input('Introduce un apellido: ')

print nombre.title(), apellido.upper()
