#Clase que hereda del objecto [object]
class Introspeccion(object):

    response = "yes"

    def __init__(self,valor):
        self._valor = valor

    def segundo(self):
        print("Segundo")

    def tercero(self):
        print("Tercero")

dato = Introspeccion("Valor")
dir(dato)

#Obtenemos información de la clase, nos muestra a que elementos de la clase
#podemos acceder
print (dir(dato))

#Nos indica si el objeto [dato] es una instancia de la clase [Introspeccion]
print (isinstance(dato,Introspeccion))

#Nos indica si el objeto [dato] tiene un determinado atributo
#En este ejemplo es False
print (hasattr(dato,"IntroVer"))

#En este ejmplo es True
print (hasattr(dato,"response"))
        


