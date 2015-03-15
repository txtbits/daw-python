# -*- coding: utf-8 -*-


def buscar_mayores_1(lista):
    '''
    1. Busca, elimina, busca: Encuentra el índice del mayor, elimina el elemento de la lista y vuelve a buscar el índice del mayor.
    '''
    copia_lista = lista[:]
    def mayor(l):
        ''' Devuelve el índice del elemento mayor'''
        i = 0
        for n, valor in enumerate(l):
            if l[i] < valor:
                i = n
        return i
    mayor1 = mayor(copia_lista)
    copia_lista.pop(mayor1)
    mayor2 = mayor(copia_lista)
    if mayor2 >= mayor1:
        mayor2 += 1
    return [mayor1,mayor2]
    
def buscar_mayores_2(lista):
    '''
    2. Ordena, identifica los elementos y devuelve sus índices.
    '''
    ''' Con .sort() hay que hacer antes una copia de la lista
    copia_lista = lista[:]
    copia_lista.sort(reverse=True)
    '''
    mayor1, mayor2 = sorted(lista, reverse=True)[:2]
    imayor1 = None  # Inicializar índices
    imayor2 = None
        
    for n, valor in enumerate(lista):  ## Mejorar
        if imayor1 == None and mayor1 == valor:
            imayor1 = n
        elif mayor2 == valor:
            imayor2 = n
        if imayor1 != None and imayor2 != None:
            break
    return [imayor1, imayor2]

    
def buscar_mayores_3(lista):
    '''
    3. Recorre la lista. Examina los valores de la lista y guarda los índices de los mayores.
    '''
    mayor1 = 0
    for n, valor in enumerate(lista):
        if lista[mayor1] < valor:
            mayor1 = n
    print 'El primer mayor es ',mayor1
    def mayor(l,m1):
        if m1 != 0:
            mayor2 = 0
        else:
            mayor2 = 1
        for n, valor in enumerate(l):
            if l[mayor2] < valor and n != m1:
                mayor2 = n
        return mayor2
    
    mayor2 = mayor(lista,mayor1)
    
    print 'el segundo mayor es ', mayor2
    return [mayor1,mayor2]