# -*- coding: utf-8 -*-
'''
Vamos a crear un programa que cree un cat�logo paralelo de amazon.es (listado de ordenadores).
En nuestro cat�logo pondremos la foto del cat�logo, el nombre del equipo y su precio, reducido en un 10% respecto a la multinacional.
'''


from amara.bindery import html
from amara.lib import U
import webbrowser
import os

# configurar bien 
#URL = 'http://www.amazon.es/s/ref=sr_abn_pp?ie=UTF8&bbn=938008031&rh=n%3A938008031'
URL = 'http://localhost/amazon_local/amazon.htm'


class Ordenador(object):
    def __init__(self, nodo):
        self.nombre = U(nodo.div[2].h3.a)
        self.precio = U(nodo.div[2].div.span)
        self.imagen = U(nodo.div[1].a.img.src)
    
        self.formato_precio(self.precio)
        self.formato_imagen(self.imagen)
    
    def formato_precio(self, precio):
        '''Convierte el precio a formato adecuado y le aplica la rebaja'''
        precio, total = precio.split("EUR ")
        self.total = float(total.replace('.', '').replace(',', '.'))
        self.rebaja = round(self.total * 0.9,2)
        
    def formato_imagen(self, imagen):
        '''Convierte la dirección de la imagen'''
        imagen, archivo = imagen.split("./amazon_files/")
        self.foto = "http://ecx.images-amazon.com/images/I/"+archivo
        
class Amazon(object):
    def __init__(self):
        self._doc = html.parse(URL)
        # Muestra los resultados 1, 2 y 3
        xpath_equipos = u'//*[@id="atfResults"]/div'
        # Muestra los resultados del 4 al 24
        xpath_equipos2 = u'//*[@id="btfResults"]/div'

        self._lista_equipos = []
        # Recorre los nodos de los resultados 1, 2, y 3
        for nodo in self._doc.xml_select(xpath_equipos):
            self._lista_equipos.append(Ordenador(nodo))
        # Recorre los nodos de los resultados del 4 al 24
        for nodo in self._doc.xml_select(xpath_equipos2):
            self._lista_equipos.append(Ordenador(nodo))

    def listado_equipos(self):
        '''Recorre los diferentes equipos'''
        for equipo in self._lista_equipos:
            print equipo.nombre
            print equipo.precio
            print equipo.rebaja
            
    def crear_html(self):
        '''Crea la tabla html donde aparece la fotografía, descripción, precio y precio rebajado en un 10%'''
        
        # Eliminar archivo.html si existe
        if os.path.exists('amazon.html'):
            os.remove('amazon.html')
        
        f = open('amazon.html', 'w')
        f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Listado de equipos Amazon</title></head><body><h1 align="center">Listado de equipos Amazon</h1><table style="border:1px dotted #000">')
        f.write('<tr bgcolor="#798a77"><td align="center">Fotografía</td><td align="center">Descripción</td><td align="center">Precio original</td><td align="center">Precio rebajado</td></tr>')
        for equipo in self._lista_equipos:
            f.write('<tr><td align="center" style="border:1px dotted #000"><img src="'+str(equipo.foto)+'"></td><td align="center" style="border:1px dotted #000">'+str(equipo.nombre)+'</td><td align="center" style="border:1px dotted #000">'+str(equipo.total)+'€</td><td align="center" style="border:1px dotted #000">'+str(equipo.rebaja)+'€</td></tr>')
        f.write('</table></body></html>')
        f.close() 
            
if __name__ == '__main__':   
    amazon = Amazon()
    amazon.listado_equipos()
    amazon.crear_html()
    webbrowser.open('amazon.html')