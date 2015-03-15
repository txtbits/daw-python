
import requests
from amara.bindery import html
from amara.lib import U

URL = 'http://www.idealista.com/pagina/inmueble?codigoinmueble=VP0000005600220&numInm=4&edd=list'
URL2 = 'http://www.idealista.com/pagina/inmueble?codigoinmueble=VP0000005027406&numInm=3&edd=list'

''' la x es de xpath '''

xpiso = '/html/body/div[2]/div/div/div/div[2]/h1'
xprecio = '//*[@id="price"]'
xmetros = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/p/strong'
xtelf = '/html/body/div[2]/div/div/div[2]/div/form/div[2]/p/strong'

#pagina = requests.get(URL)
doc = html.parse(URL) #(pagina.content.decode('utf-8'))

print U(doc.xml_select(xpiso)[0]).strip()
print U(doc.xml_select(xprecio)[0]).strip()
print U(doc.xml_select(xmetros)[0]).strip()
print U(doc.xml_select(xtelf)[0]).strip()
