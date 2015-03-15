# -*- coding: utf-8 -*-


import sqlite3 as dbapi
import webbrowser



def insertar(conexion):
    micursor = conexion.cursor()
    INSERT = """insert into empleados
                  values (?, ?, ?)"""
    
    for n in range(100):
        micursor.execute(INSERT, ('12345678' + str(n), 'Empleado_' + str(n), 'Empleados satisfechos'))
    
    # commit del insert
    conexion.commit()
    
    # cierro cursor
    micursor.close()


def muestra_resultados(conexion):
    cursor = conexion.cursor()
    cursor.execute('select * from empleados')
    for empleado in cursor.fetchall():
        print empleado
        
    cursor.close()
    
def crea_tabla(conexion):
    '''Devuelve los resultados de la consulta en una tabla html. El fichero se llamará empleados.html'''
    # abrir cursor
    cursor = conexion.cursor()
    # realizar consulta
    cursor.execute('select * from empleados')
    # abrir fichero
    f = open('empleados.html', 'w')
    # insertar cabeceras
    f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Empleados BBDD</title></head><body><h1 align="center">Listado de empleados</h1><table style="border:1px solid #000">')
    f.write('<tr>')
    for col in cursor.description:
        f.write('<th bgcolor="#798a77">%s</th>' %col[0])  
    f.write('</tr>')      
    
    # filas de la tabla
    for linea in cursor.fetchall():
        f.write('<tr>')
        for dato in linea:
            f.write('<td>%s</td>' %  dato)
        f.write('</tr>')
    
    # cierre fichero    
    f.write('</table></body></html>')
    f.close()
    cursor.close()
    
if __name__ == '__main__':
    # conexion con la basde de datos alumnos
    conexion = dbapi.connect(r'empleados.bd')
    
    # función que inserta 100 empleados
    insertar(conexion)
    
    # mostrar
    muestra_resultados(conexion)
    
    # crear fichero con una tabla html
    crea_tabla(conexion)
    
    webbrowser.open('empleados.html')
    
    conexion.close()