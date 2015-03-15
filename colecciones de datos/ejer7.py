# -*- coding: utf-8 -*-
'''
Escribe un programa que pida una lista de nombres (acabada con un <intro>).
El programa mostrará la lista de nombres en orden alfabético sin repetir ninguno.
'''

'''
agenda = []

persona = ['Luis Pérez', 'luisperez@micorreo.com', '666666666']

persona2 = ['María Aznar', 'mariaaznar@micorreo.com', '699887766']

agenda.append(persona)

agenda.append(persona2)

for contacto in agenda:
    print "%-20s %-20s" % (contacto[0], contacto[1])

print '------------------------------'

for contacto in agenda:
    if 'Luis' in contacto[0]:
        print contacto[0], contacto[2]
'''


def add_contactos(agenda):
    n_cont = int(raw_input('¿Cuántos contactos quieres introducir?: '))
    for x in range(n_cont):
        contacto = ['','','']
        contacto[0] = raw_input('Introduce el nombre: ')
        contacto[1] = raw_input('Introduce el correo: ')
        contacto[2] = raw_input('Introduce el teléfono: ')
        agenda.append(contacto)
        print agenda
        
def listado_contactos(agenda):
    for cto in agenda:
        print cto

def buscar_contactos(agenda):
    busqueda = raw_input('Introduce el contacto que buscas: ')
    for contacto in agenda:
        if busqueda in contacto[0]:
            print contacto
        else:
            print 'Contacto no encontrado'
        
agenda = []

add_contactos(agenda)
listado_contactos(agenda)
buscar_contactos(agenda)
