# -*- coding: utf-8 -*-
'''
Created on 10/02/2012

@author: Alumno
'''
from inaem import *
from amara.bindery import html
from amara.bindery import parse

#abril
CURSO1 = '''<tr><td class="textoApl1"><a alt="Pulse para acceder al contenido del curso" title="Pulse para acceder al contenido del curso" href="http://plan.aragon.es/MapaRec.nsf/%28ID%29/B9A014F59B05533EC1257976002C4C0C?OpenDocument" class="enlaceApl1 pequena1 negrita">ADOBE PHOTOSHOP</a></td><td alt="Modalidad del curso" title="Modalidad del curso" class="negro pequena1 izquierda">Presencial</td><td alt="Alumnos por curso" title="Alumnos por curso" class="negro pequena1 centrado">15</td><td alt="Horas por curso" title="Horas por curso" class="negro pequena1 centrado">50</td><td alt="Localidad donde se imparte el cuso" title="Localidad donde se imparte el cuso" class="negro pequena1 negro izquierda">Zaragoza</td><td alt="Fecha prevista de inicio" title="Fecha prevista de Inicio" acronym="" class="negro pequena1 padding3 ">Abril 2012 Tarde</td></tr>'''
#10/04/2012
CURSO2 = '''<tr><td class="textoApl1" style="background-color: rgb(248, 247, 247);"><a alt="Pulse para acceder al contenido del curso" title="Pulse para acceder al contenido del curso" href="http://plan.aragon.es/MapaRec.nsf/%28ID%29/7125019113255846C12578A70036DBA5?OpenDocument" class="enlaceApl1 pequena1 negrita">ADMINISTRACIÓN AVANZADA DE S.O. RED HAT LINUX - NIVEL CERTIFIED ENGINEER CERTIFICACIÓN RHCE (M)</a></td><td alt="Modalidad del curso" title="Modalidad del curso" class="negro pequena1 izquierda" style="background-color: rgb(248, 247, 247);">Presencial</td><td alt="Alumnos por curso" title="Alumnos por curso" class="negro pequena1 centrado" style="background-color: rgb(248, 247, 247);">15</td><td alt="Horas por curso" title="Horas por curso" class="negro pequena1 centrado" style="background-color: rgb(248, 247, 247);">80</td><td alt="Localidad donde se imparte el cuso" title="Localidad donde se imparte el cuso" class="negro pequena1 negro izquierda" style="background-color: rgb(248, 247, 247);">Zaragoza</td><td title="Fecha de Inicio" acronym="" class="negro pequena1 padding3 " style="background-color: rgb(248, 247, 247);">10/04/2012-10/05/2012</td></tr>'''

def test_inicio_mes_nombre():
    doc = parse(CURSO1)
    curso = Curso(doc.tr)
    assert curso.comienza('abril') == True
    assert curso.comienza('Abril') == True
    assert curso.comienza('marzo') == False

def test_inicio_mes_numero():    
    doc = parse(CURSO2)
    curso = Curso(doc.tr)
    assert curso.comienza('abril') == True
    assert curso.comienza('Abril') == True
    assert curso.comienza('marzo') == False