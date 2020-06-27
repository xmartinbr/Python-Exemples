lista = [2,4]

try:
    print(lista[1])
except IndexError:
    print ("Error: error en el indice")
else:
    print ("No hay error")
finally:
    print ("Se ejecuto")

#Lanzar una excepcion
try:
    raise TypeError
except:
    print("Errores con los tipos")


#Crear una excepcion por el usuario
class myErr(Exception):
    def __init__(self, valor):
        print ("Fue el error por,", valor)

try:
    raise myErr(4)
except myErr:
    print ("Error escrito:")
        


