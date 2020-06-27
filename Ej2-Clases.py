#Clase que hereda del objecto [object]
class Circulo(object):

#Decorador utilizado para indicar que estamos declarando una propiedad
    @property
    def area(self):
        return (3.1416*(self._radio**2))
    
#constructor
#Con el 1º parámetro [self] podemos acceder a las variables de instancia
#que serán utilizadas máas tarde en otros métodos
    def __init__(self,radio):
        self._radio = radio


class Triangulo(object):

    @property
    def area(self):
        return ((self._base*self._altura)/2)

    def __init__(self,base,altura):
        self._base = base
        self._altura = altura

#Ejemplo de polimorfismo
def calcular(figura):
    print(figura.area)

c = Circulo(10)
t = Triangulo(5,4)

print("Circulo: ")
calcular(c)
print("Triangulo: ")
calcular(t)


