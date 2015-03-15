# -*- coding: utf-8 -*-


import sqlite3 as bd
import matplotlib.pyplot as plt
# crear basde de datos de ciclistas

# crear tablas

# insertar datos

def crea_inserta(conexion):
    datos = open('ciclismo_BD.sql').read()
    cursor = conexion.cursor()
    for sentencia in datos.split(';'):
        cursor.execute(sentencia)
    
    conexion.commit()
    cursor.close()

def consulta(conexion, sql):
    cursor = conexion.cursor()
    cursor.execute(sql) 
    cols = len(cursor.description)
    tam = 80 / cols
    encabezado = [d[0] for d in cursor.description]
    for col in encabezado:
        print "%-*s" % (tam,col),
    print
    print '_'*80
    for linea in cursor.fetchall():
        print linea

    cursor.close()


def grafico(conexion, sql):
    cursor = conexion.cursor()
    cursor.execute(sql)
    
    plt.ylabel('ALTURA')
    plt.xlabel('PUERTO')
    puerto = []
    altura = []
    for linea in cursor.fetchall():
        puerto.append(linea[0])
        altura.append(linea[1])
    print puerto
    print altura
    plt.bar(range(len(altura)),altura)
    plt.xticks(range(len(altura)), puerto)
    plt.show()
    

if __name__ == '__main__':
    conexion = bd.connect('ciclistas.dat')
    #crea_inserta(conexion)
    cons = 'select * from maillot'
    #consulta(conexion, cons)
    grafico(conexion,'select nompuerto,altura from puerto')
    conexion.close()