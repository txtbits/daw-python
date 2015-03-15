# -*- coding: utf-8 -*-

from amara.bindery import html
from amara.lib import U

URL = 'http://172.30.167.1/inaem/fmrListado.html'

doc = html.parse(URL)

#print doc.xml_encode()


xpath_cursos = '/html/body/form/table/tbody/tr'

lista_cursos = doc.xml_select(xpath_cursos)

'''
for curso in lista_cursos[1:]:
    if 'WEB' in U(curso.td).upper() and U(curso.td[4]).lower() == u'zaragoza':
        print curso.td, curso.td[4]#curso.td.a.href
'''

for curso in lista_cursos[1:]:
    if U(curso.td[4]).lower() == u'zaragoza' and 'abril' in U(curso.td[5]).lower():
        print curso.td, curso.td[4], curso.td[5]