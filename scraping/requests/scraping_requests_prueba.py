
import requests
from amara.bindery import html
import urlparse

URL = 'http://pepinon.inf.enlaces/compartido/'

pagina = requests.get(URL)

'''print pagina.headers'''

open(r'C:\Users\Alumno\Desktop\pagina.html', 'w').write(pagina.content)

doc = html.parse(pagina.content)

'''print doc.xml_encode()'''

enlaces = u'//tr/td/a'
lista_enlaces = doc.xml_select(enlaces)

print len(lista_enlaces)

for enlace in lista_enlaces:
    print enlace, urlparse.urljoin(URL, enlace.href)



