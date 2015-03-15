# -*- coding: cp1252 -*-

def dibuja_tablero(pantalla):   # dibujamos las lineas del tablero
    Line(Point(1, 0), Point(1, 3)).draw(pantalla)
    Line(Point(2, 0), Point(2, 3)).draw(pantalla)
    Line(Point(0, 1), Point(3, 1)).draw(pantalla)
    Line(Point(0, 2), Point(3, 2)).draw(pantalla)

def celda(punto):   # calculamos el número de celda en el que hacen clic los jugadores
    x, y = punto.x, punto.y
    x = int(x)
    y = int(y)
    return x + y*3 +1

def gana(tablero, ficha):   # se compara una lista de posiciones ganadoras con una ficha y si hay ganador, se devuelve un True
    lista_ganadoras = [[1, 2, 3],[1, 4, 7],[1, 5, 9], [3, 5, 7], [3, 6, 9], [2, 5, 8], [4, 5, 6],[7, 8, 9]]
    for linea in lista_ganadoras:
        if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]] == ficha:
            return True
    return False

def dibuja_ficha(pantalla, ficha, c):   # función para dibujar las fichas en el tablero
    puntos = [
    Point(0.5, 0.5),Point(1.5, 0.5),Point(2.5, 0.5),
    Point(0.5, 1.5),Point(1.5, 1.5),Point(2.5, 1.5),
    Point(0.5, 2.5),Point(1.5, 2.5),Point(2.5, 2.5)]
    
    p1_lineas1 = [
    Point(0.25,0.75),Point(1.25,0.75),Point(2.25,0.75),
    Point(0.25,1.75),Point(1.25,1.75),Point(2.25,1.75),
    Point(0.25,2.75),Point(1.25,2.75),Point(2.25,2.75),
    ]
    
    p2_lineas1 = [
    Point(0.75,0.25),Point(1.75,0.25),Point(2.75,0.25),
    Point(0.75,1.25),Point(1.75,1.25),Point(2.75,1.25),
    Point(0.75,2.25),Point(1.75,2.25),Point(2.75,2.25),
    ]

    p1_lineas2 = [
    Point(0.25,0.25),Point(1.25,0.25),Point(2.25,0.25),
    Point(0.25,1.25),Point(1.25,1.25),Point(2.25,1.25),
    Point(0.25,2.25),Point(1.25,2.25),Point(2.25,2.25),
    ]
    
    p2_lineas2 = [
    Point(0.75,0.75),Point(1.75,0.75),Point(2.75,0.75),
    Point(0.75,1.75),Point(1.75,1.75),Point(2.75,1.75),
    Point(0.75,2.75),Point(1.75,2.75),Point(2.75,2.75),
    ]
    
    if ficha == 'O':    # si la ficha es la 'O', se dibuja un circulo en la posicion correspondiente
        Circle(puntos[c-1], 0.25).draw(pantalla)
    elif ficha == 'X': # si es la 'X', se dibuja una equis dónde corresponde
        Line(p1_lineas1[c-1],p2_lineas1[c-1]).draw(pantalla)
        Line(p1_lineas2[c-1],p2_lineas2[c-1]).draw(pantalla)


def mueve_maquina(tab):
    lista_ganadoras = [[1, 2, 3],[1, 4, 7],[1, 5, 9], [3, 5, 7], [3, 6, 9], [2, 5, 8], [4, 5, 6],[7, 8, 9]]
    pos = -1
    
    # si la quinta posición del vector tablero está vacía, la máquina mueve si ficha ahí
    if tab[5] == ' ': 
        pos = 5
        return pos
    else:
        # si no, mira a ver si puede ganar y si puede, lo hace
        for pos_gana in lista_ganadoras:    
            if tab[pos_gana[0]] == tab[pos_gana[1]] == 'O' and tab[pos_gana[2]] == ' ':
                pos = pos_gana[2]
                return pos
            elif tab[pos_gana[1]] == tab[pos_gana[2]] == 'O' and tab[pos_gana[0]] == ' ':
                pos = pos_gana[0]
                return pos
            elif tab[pos_gana[0]] == tab[pos_gana[2]] == 'O' and tab[pos_gana[1]] == ' ':
                pos = pos_gana[1]
                return pos

        # si pos < 0, quiere decir que ni ha movido al centro ni ha podido ganar, con lo cual ahora toca ver si el otro jugador puede ganar   
        if pos < 0: 
            for pos_gana in lista_ganadoras:
                if tab[pos_gana[0]] == tab[pos_gana[1]] == 'X' and tab[pos_gana[2]] == ' ':
                    pos = pos_gana[2]
                    return pos
                elif tab[pos_gana[1]] == tab[pos_gana[2]] == 'X' and tab[pos_gana[0]] == ' ':
                    pos = pos_gana[0]
                    return pos
                elif tab[pos_gana[0]] == tab[pos_gana[2]] == 'X' and tab[pos_gana[1]] == ' ':
                    pos = pos_gana[1]
                    return pos
        # si pos < 0, tampoco podía ganar el jugador 'X' así que intenta poner una ficha en las esquinas
        if pos < 0:
            for x in range(1, 10, 2):
                if x != 5:
                    if tab[x] == ' ':
                        pos = x
                        print pos
                        return pos

        # si llega aquí, ya sólo queda mover la ficha a una de las posiciones centrales (2,4,6 y 8)              
        if pos < 0:
            for x in range(2, 9, 2):
                if tab[x] == ' ':
                    pos = x
                    print pos
                    return pos
                    
                     
from graphics import *
from time import sleep
from random import randint

#Creamos la ventana gráfica y le asignamos las coordenadas
pantalla = GraphWin('Tres en raya', 300, 300)
pantalla.setCoords(0,0,3,3)
tablero = [' '] *10
tablas = True

modo = int(raw_input('''
Elige el modo de juego
1. Jugador 1 vs Jugador 2 (Pulsa 1 y enter)
2. Jugador vs Ordenador (Pulsa 2 y enter)
'''))
dibuja_tablero(pantalla)
ficha = ' '
if modo == 1:
    x = 0
    while ' ' in tablero[1:]: #mientras haya un espacio en blanco en tablero, seguirá ejecutando el programa
        p = pantalla.getMouse()
        c = celda(p)    # llama a la funcion celda, para averiguar la celda en la que toca poner la ficha
        if tablero[c] ==  ' ': 
            if x % 2:   # si el resto es 0, le toca mover al jugador 1, si no al 2
                ficha = 'X'
            else:
                ficha = 'O'
            tablero[c] = ficha      # llena la posición del tablero con la ficha correspondiente
            dibuja_ficha(pantalla, ficha, c)    #dibuja la ficha en pantalla
            print tablero
            x +=1
            
        else:
            print 'Casilla ocupada'
        if gana(tablero, ficha):    # comprueba si hay ganador
            print 'Has ganado'
            tablas = False
            break
    if tablas:
        print 'Tablas'
elif modo == 2:
    x = 2
    ficha = ' '
    while ' ' in tablero[1:]: #mientras haya un espacio en blanco en tablero, seguirá ejecutando el programa
        if x % 2 == 0:  # si el resto es 0, mueve el jugador, si no la máquina
            p = pantalla.getMouse()
            c = celda(p) # llama a la funcion celda, para averiguar la celda en la que toca poner la ficha
            ficha = 'X'
            if tablero[c] ==  ' ':
                tablero[c] = ficha      # llena la posición del tablero con la ficha correspondiente
                dibuja_ficha(pantalla, ficha, c)    #dibuja la ficha en pantalla
                x += 1
            else:
                print 'Casilla ocupada'
        else:
            ficha = 'O'
            # genero un número aleatorio de espera para que las fichas no salgan automáticamente
            tiempo = randint(10,20)
            tiempo = tiempo * 0.1
            sleep(tiempo)
            pos = mueve_maquina(tablero)
            tablero[pos] = 'O'  # llena la posición del tablero con la ficha correspondiente
            dibuja_ficha(pantalla, ficha, pos)  #dibuja la ficha en pantalla
            x += 1
        print tablero
        if gana(tablero, 'X'):  # se comprueba si gana el jugador o la máquina
            print 'Has ganado'
            tablas = False
            break
        elif gana(tablero, 'O'):
            print 'Gana la maquina'
            tablas = False
            break
    # Si nadie gana, se imprime un mensaje de tablas 
    if tablas:
        print 'Tablas'
