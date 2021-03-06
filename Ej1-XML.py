#Del package xml.dom.minidom
#importamos 2 módulos, módulo (parse) y módulo (Node)
from xml.dom.minidom import parse, Node

#Contenido de l fichero 'note.xml'
# <?xml version="1.0" encoding="UTF-8"?>
# <res>
#	<ruta>Ave Principal #346</ruta>
#	<pro>Sara</pro>
#	<pro>Miguel</pro>
#	<pro>Javi</pro>
# </res>
xmltree=parse('note.xml')

#Recorremos todos los nodos <pro> y por cada uno de ellos
#haremos un recorrido por sus nodos hijos y validamos su tipo,
#si son de tipo TEXTO imprimiremos su contenido
for nodo in xmltree.getElementsByTagName('pro'):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType == Node.TEXT_NODE:
            print(nodo_hijo.data)

