# -*- coding: utf-8 -*-

'''
Created on 07/02/2012

@author: Alberto
'''

from amara.bindery import html
from amara.lib import U

URL = 'http://plan.aragon.es/maparec.nsf/fmrListado?OpenForm'
#URL = 'http://localhost/inaem'

class Curso(object):
    def __init__(self, nodo):
        self.nombre = U(nodo.td).title()
        self.modalidad = U(nodo.td[1])
        self.alumnos = U(nodo.td[2])
        self.horas = U(nodo.td[3])
        self.localidad = U(nodo.td[4])
        self.inicio = U(nodo.td[5])
        self.leer_especialidad(nodo.td.a.href)
        
    def leer_especialidad(self, href):
        URL = href
        doc = html.parse(URL)
        xpath = u'/html/body/form/fieldset[2]/div[2]/div[2]'
        self.especialidad = U(doc.xml_select(xpath))
        # debug
        # print self.especialidad
        
class Inaem(object):
    def __init__(self):
        self._doc = html.parse(URL)
        xpath_cursos = u'/html/body/form/table/tbody/tr'
        # primer elemento es cabecera
        self._lista_cursos = []
        for nodo in self._doc.xml_select(xpath_cursos)[1:]:
            self._lista_cursos.append(Curso(nodo))
            
        
    def listado_cursos(self):
        '''Imprime en pantalla el listado de los curso de la 
        p�gina del INAEM'''
        
        for curso in self._lista_cursos:
            # nombre del curso en primer td
            print curso.nombre
            
    def listado_cursos_veces(self):
        ''' Muestra el listado de cursos con el numero de veces
        que se repiten'''
        
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso.nombre] = cursos.get(curso.nombre, 0) + 1
        nombres = cursos.keys()
        nombres.sort()
        for clave in nombres:
            print clave, cursos[clave] # pinta nombre y repeticiones
            
    def listado_cursos_meses(self):
        '''Muestra el listado de cursos agrupado por meses'''
        
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso.inicio] = curso.nombre
        fechas = cursos.keys()
        fechas.sort()
        for clave in fechas:
            print clave, cursos[clave]
    
    def listado_manana_tarde(self):
        '''Muestra la cantidad de cursos de ma�ana y de tarde'''
        tardes = 0
        manana = 0
        for curso in self._lista_cursos:
            if "Tarde" in curso.inicio:
                tardes += 1
            elif "Ma�ana" in curso.inicio:
                manana += 1
        
        print "Cursos de Ma�ana: "+str(manana)+"\nCursos de Tarde: "+str(tardes)
        
    def listado_localidad(self):
        '''Muestra la cantidad de cursos por localidad'''
        
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso.localidad] = cursos.get(curso.localidad, 0) + 1
        localidad = cursos.keys()
        localidad.sort()
        for clave in localidad:
            print clave, cursos[clave]
            
    def listado_familias_pro(self):
        '''Muestra un listado de cursos por familia profesional'''
        
        cursos = {}
        for curso in self._lista_cursos:
            cursos[curso.nombre] = curso.especialidad
        espec = cursos.keys()
        espec.sort()
        for clave in espec:
            print clave, cursos[clave]
        
    def generar_html(self):
        '''Genera HTML con la informaci�n de los nombres de cursos de inform�tica,
        la poblaci�n y el mes de inicio'''
        f = open('inaem.html', 'w')
        f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Cursos INAEM</title></head><body><h1 align="center">Listado de Cursos INAEM</h1><table border="1" bordercolor="#666" cellpadding="10" align="center">')
        f.write('<tr bgcolor="#FE2E2E"><td>Nombre del Curso</td><td>Poblaci�n</td><td>Mes de inicio</td></tr>')
        for curso in self._lista_cursos:
            f.write('<tr><td>'+str(curso.nombre)+'</td><td">'+str(curso.localidad)+'</td><td>'+str(curso.inicio)+'</td></tr>')
            
        f.write('</table></body></html>')
        f.close() 
    
    
    
if __name__ == '__main__':
    inaem = Inaem()  # crea un objeto con nuestra clase
    print "*" * 40
    print "Listado alfabetico de todos los cursos con el numero de veces"
    print "*" * 40
    inaem.listado_cursos_veces()
    print "*" * 40
    print "Listado de cursos agrupado por meses de inicio"
    print "*" * 40
    inaem.listado_cursos_meses()
    print "*" * 40
    print "�Cu�ntos cursos hay de ma�ana y cu�ntos de tarde?"
    print "*" * 40
    inaem.listado_manana_tarde()
    print "*" * 40
    print "�Cu�ntos hay en cada localidad?"
    print "*" * 40
    inaem.listado_localidad()
    print "*" * 40
    print "Listado de cursos organizados por familias profesionales"
    print "*" * 40
    inaem.listado_familias_pro()
    
    inaem.generar_html()