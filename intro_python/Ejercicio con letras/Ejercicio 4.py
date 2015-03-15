# -*- coding: cp1252 -*-
'''
Pide a un usuario que escriba su nombre y su apellido.
Tú lo mostrarás correctamente: El nombre con las iniciales el mayúsculas
y el apellido todo en mayúsculas, aunque el usuario no lo haya escrito así.
'''

nombre = raw_input('Introduce un nombre: ')
apellido = raw_input('Introduce un apellido: ')

print nombre.title(), apellido.upper()
