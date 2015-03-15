# -*- coding: utf-8 -*-

'''
Escribe un programa en python usando dbapi y matplotlib que genere un informe a partir de la base de datos de ciclismo en sqlite.
Características del informe:
Tendrá cinco sub-informes (cinco consultas en la base de datos)

    El informe se mostrará en html
    Los datos resultantes de la consulta se mostrarán en una tabla debidamente formateada
    Se hará una gráfica de cada informe con matplotlib.
    Los gráficos serán diferentes (barras, sectores, barras horizontales)
    El html tendrá enlazada una hoja de estilos .css
    En el html crearemos un índice con enlaces a los cinco informes.

'''

import os
import sqlite3 as bd
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter

def consulta(conexion, cons):
    cursor = conexion.cursor()
    cursor.execute(cons)
    enc = [d[0] for d in cursor.description]
    res = cursor.fetchall()
    return [enc, res]
    
def grafico_barras(encabezado,dat):
    plt.ylabel('ALTURA')
    plt.xlabel('PUERTO')
    puerto = []
    altura = []
    for linea in dat:
        puerto.append(linea[0])
        altura.append(linea[1])
    plt.bar(range(len(altura)),altura)
    plt.xticks(range(len(altura)), puerto, rotation="vertical")
    savefig('grafico1.png')
    #show()


def grafico_sectores(conexion,dat):
    ciclistas = []
    etapas = []
    for linea in dat:
        ciclistas.append(linea[0])
        etapas.append(linea[1])
    figure(2, figsize=(10,10))
    pie(ciclistas, labels=etapas, autopct='%1.1f%%',pctdistance=1.1,labeldistance=1.2)
    title('PORCENTAJE DE CICLISTAS QUE HAN GANADO ETAPAS')
    savefig('grafico2.png')
    #show()
    
def grafico_plot(conexion,dat):
    dorsal = []
    edad = []
    for linea in dat:
        dorsal.append(linea[0])
        edad.append(linea[1])
    plot(dorsal,edad)
    ylabel('Edad')
    xlabel('Dorsal')
    savefig('grafico3.png')
    #show()
   
def grafico_3d(conexion,dat):
    fig = figure()
    ax = fig.gca(projection='3d')
    x = np.linspace(0, 1, 100)
    y = np.sin(x * 2 * np.pi) / 2 + 0.5
    ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')
    colors = ('r', 'g', 'b', 'k')
    for c in colors:
        x = np.random.sample(4)
        y = np.random.sample(4)
        ax.scatter(x, y, 0, zdir='y', c=c)
    ax.legend("A")
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    ax.set_zlim3d(0, 1)
    savefig('grafico4.png')
    #show()
   
def graficoprueba(conexion,dat):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    cc = lambda arg: colorConverter.to_rgba(arg, alpha=0.6)
    lista = []
    for linea in dat:
        lista.append(linea[2])
    xs = np.arange(0, 10, 0.4)
    verts = []
    zs = [0.0, 1.0, 2.0, 3.0]
    for z in zs:
        ys = np.random.rand(len(lista))
        ys[0], ys[-1] = 0, 0
        verts.append(zip(xs, ys))
    poly = PolyCollection(verts, facecolors = [cc('r'), cc('g'), cc('b'),                                         cc('y')])
    poly.set_alpha(0.7)
    ax.add_collection3d(poly, zs=zs, zdir='y')
    ax.set_xlabel('X')
    ax.set_xlim3d(0, 10)
    ax.set_ylabel('Y')
    ax.set_ylim3d(-1, 4)
    ax.set_zlabel('Z')
    ax.set_zlim3d(0, 1)
    savefig('grafico5.png')
    #show() 
    
def crear_html():
    '''Crea la tabla html'''
    
    # Eliminar archivo.html si existe
    if os.path.exists('grafico.html'):
        os.remove('grafico.html')
    
    f = open('grafico.html', 'w')
    f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Graficos ciclistas</title></head><body><h1 align="center">Graficos ciclistas</h1><table style="border:1px dotted #000">')
    f.write('<ul>')
    f.write('<li><img src="grafico1.png"/></li>')
    f.write('<li><img src="grafico2.png"/></li>')
    f.write('<li><img src="grafico3.png"/></li>')
    f.write('<li><img src="grafico4.png"/></li>')
    f.write('<li><img src="grafico5.png"/></li>')
    f.write('</ul>')
    f.write('</body></html>')
    f.close() 


if __name__ == '__main__':
    conexion = bd.connect('ciclistas.dat')
    
    '''
    NOTA: Dejo comentadas las sentencias, dado que al modificar valores de ejes etc, los graficos
    salen los graficos mal, por tanto hay que generar los graficos de uno en uno.
    '''
    
    #encabezado, datos = consulta(conexion,'select nompuerto,altura from puerto')
    #grafico_barras(encabezado, datos)
    
    #encabezado, datos = consulta(conexion, 'select dorsal, edad from ciclista')
    #grafico_plot(encabezado, datos)
    
    #encabezado, datos = consulta(conexion, 'select count(etapa.netapa), ciclista.nombre from etapa join ciclista on etapa.dorsal = ciclista.dorsal group by ciclista.nombre')
    #grafico_sectores(encabezado, datos)
    
    #encabezado, datos = consulta(conexion, "select dorsal, nomeq from ciclista ")
    #grafico_3d(encabezado, datos)
    
    #encabezado, datos = consulta(conexion, 'select * from llevar where dorsal in (1,22,20)')
    #graficoprueba(encabezado, datos)  
    
    crear_html()