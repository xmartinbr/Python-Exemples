#Del xml.etree.ElementTree
#importamos 1 módulo, módulo (parse)
from xml.etree.ElementTree import parse
import xml.sax

#Contenido de l fichero 'note.xml'
# <?xml version="1.0" encoding="UTF-8"?>
# <res>
#	<ruta>Ave Principal #346</ruta>
#	<pro>Sara</pro>
#	<pro>Miguel</pro>
#	<pro>Javi</pro>
# </res>
xml_doc = parse('note.xml')

#Recorremos todos los nodos <pro> y por cada uno de ellos
#haremos un recorrido por sus nodos hijos y validamos su tipo,
#si son de tipo TEXTO imprimiremos su contenido
for nodo in xml_doc.findall('pro'):
    print(nodo.text)

