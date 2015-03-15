# -*- coding: utf-8 -*-
'''
A partir de la información general de cursos del INAEM (http://plan.aragon.es/maparec.nsf/general), nos piden un programa que realice las siguientes tareas:

1. Listado alfabético de todos los cursos (sin repeticiones). Al lado de cada curso indicaremos el número de veces que aparece en el listado si aparece más de una vez.
2. Listado de cursos agrupado por meses de inicio.
3. ¿Cuántos cursos hay de mañana y cuántos de tarde?
4. ¿Cuántos hay en cada localidad?
5. Listado de cursos organizados por familias profesionales (Informática ...) Pista. Fíjate en el link que abre cada curso.
6. Grabación de un archivo en formato html (una tabla) con la información de los nombres de cursos de informática, la población y el mes de inicio.
'''


from amara.bindery import html
from amara.lib import U

# configurar bien 
URL = 'http://plan.aragon.es/maparec.nsf/fmrListado?OpenForm'
#URL = 'http://localhost/lmarcas/inaem.htm'


class Curso(object):
    def __init__(self, nodo):
        self.nombre = U(nodo.td).title()
        self._nodo = nodo
        self._inicio = ''  # guardaremos la fecha de inicio "cruda"
        self._get_inicio()
        self.localidad = U(nodo.td[4]).title()
        url_familia = 'http://plan.aragon.es' + U(nodo.td.a.href)
        print url_familia
        self._doc = html.parse(url_familia)
        xpath_cur_fam = u'/html/body/form/fieldset[2]/div[2]'
        nosecomollamarla = self._doc.xml_select(xpath_cur_fam)
        self.familia = U(nosecomollamarla.div[2])
        
    def _get_inicio(self):
        self._inicio = U(self._nodo.td[5]) # cargar información de inicio
        if '-' in self._inicio:
            self._inicio = self._inicio.split('-')[0]
            
    def comienza(self, mes):
        """Devuelve verdadero o falso, si el curso comienza en el mes indicado"""
        meses = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4}
        num_mes = meses.get(mes.lower(), 0)
        
        return mes.lower() in self._inicio.lower() or '/%02d/' % num_mes in self._inicio
    
    def __str__(self):
        return self.nombre + ' (' + self._inicio + ')'

class Inaem(object):
    def __init__(self):
        self._doc = html.parse(URL)
        xpath_cursos = u'/html/body/form/table/tbody/tr'
        # primer elemento es cabecera
        self._lista_cursos = []
        for nodo in self._doc.xml_select(xpath_cursos)[1:]:
            self._lista_cursos.append(Curso(nodo))
            
    def listado_cursos(self):
        '''Imprime en pantalla el listado de los curso de la página del INAEM'''
        for curso in self._lista_cursos:
            # nombre del curso en primer td
            print curso.nombre
            
    def lista_cursos_veces(self):
        ''' Muestra el listado de cursos con el numero de veces que se repiten'''
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso.nombre] = cursos.get(curso.nombre, 0) + 1
        nombres = cursos.keys()
        nombres.sort()
        for clave in nombres:
            print clave, cursos[clave]   # imprime nombre y repeticiones

    def listado_cursos_meses(self):
        '''Muestra el listado de cursos agrupado por meses de inicio'''
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso._inicio] = curso.nombre
        fechas = cursos.keys()
        fechas.sort()
        for clave in fechas:
            print clave, cursos[clave]
    
    def listado_jornada(self):
        '''Muestra la cantidad de cursos de mañana y de tarde'''
        tardes = 0
        manana = 0
        for curso in self._lista_cursos:
            if "Tarde" in curso._inicio:
                tardes += 1
            elif "MaÃ±ana" in curso._inicio: # Problema con la codificación de la Ñ
                manana += 1
        print "Cursos en horario de Mañana: "+str(manana)+"\nCursos en horario de Tarde: "+str(tardes)
    
    def listado_localidad(self):
        '''Muestra la cantidad de cursos por localidad'''
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso.localidad] = cursos.get(curso.localidad, 0) + 1
        localidad = cursos.keys()
        localidad.sort()
        for clave in localidad:
            print clave, cursos[clave]

    def listado_familias(self):
        '''Muestra un listado de cursos por familia profesional'''
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso.nombre] = curso.familia
        familia = cursos.keys()
        familia.sort()
        for clave in familia:
            print clave, cursos[clave]
    
    def grabacion_html(self):
        '''Genera una tabla HTML'''
        f = open('inaem.html', 'w')
        f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Cursos INAEM</title></head><body><h1 align="center">Listado de Cursos INAEM</h1><table style="border:1px solid #000">')
        f.write('<tr bgcolor="#798a77"><td>Nombre del Curso</td><td>Población</td><td>Mes de inicio</td></tr>')
        for curso in self._lista_cursos:
            if 'INFORMÁTICA' in curso.familia: 
                f.write('<tr><td>'+str(curso.nombre)+'</td><td>'+str(curso.localidad)+'</td><td>'+str(curso._inicio)+'</td></tr>')
            
        f.write('</table></body></html>')
        f.close() 

if __name__ == '__main__':
    inaem = Inaem()  # crea un objeto con nuestra clase
    
    #inaem.listado_cursos()
    
    ''' Ejercicio 1 '''
    #inaem.lista_cursos_veces()
    
    ''' Ejercicio 2 '''
    #inaem.listado_cursos_meses()
    '''
    for curso in inaem._lista_cursos:
        if curso.comienza('abril'):
            print curso
    '''
    
    ''' Ejercicio 3 '''
    #inaem.listado_localidad()
    
    ''' Ejercicio 4 ''' 
    #inaem.listado_jornada()
    
    ''' Ejercicio 5 '''
    #inaem.listado_familias()
    
    ''' Ejercicio 6 '''
    #inaem.grabacion_html()
    
    print "TERMINADO" # para saber que ha terminado, porque con lo que tarda....puf
