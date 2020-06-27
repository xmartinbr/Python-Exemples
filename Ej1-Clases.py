#Clase que hereda del objecto [object]
class Persona(object):
    nombre = "Juan"
    
    def __new__(cls):
        print("New... 1º método llamado al crear un obj.")
        return super(Persona,cls).__new__(cls)

#constructor
#Con el 1º parámetro [self] podemos acceder a las variables de instancia
    def __init__(self):
        self.saludo = "En castellano"
        print("Init... 2º método llamada al crear un obj.")
    
#método de instancia
#Con el 1º parámetro [self] podemos acceder a la variable [saludo]
#declarada préviamente en el método __init__
    def despedir(self):
        print("Adios " + self.saludo)

#decorador utilizado para indicar que un método es de clase y
#no de instancia
#Con el 1º parámetro [cls] podemos acceder a las variables estáticas de la clase
    @classmethod
    def saludar(cls, apellido):
        print("Estoy saludando a " + cls.nombre + " " + apellido)

#decorador utilizado para indicar que un método es estático
#No tiene acceso a variables de ningún tipo, ni de clase ni de instancia
    @staticmethod
    def nadar(opt):
        print("Nado Paso: " + opt)

#Llamada a un método de clase
Persona.saludar("Rodriguez")

#Se crea el obj.
my = Persona()

#Llamada a un método estático
Persona.nadar('1')

#Llamada a un método estático
my.nadar('2')

my.despedir()
