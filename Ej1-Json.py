import json

with open('note.json') as myFile:
    data = json.load(myFile)

print(data)
print(data["clientesA"])

#La clausula 'with' sólo puede ser utilizada con objetos de tipo
#(Context Manager)
#Este tipo de objetos debe implementar como mínimo 2 métodos:
#   __enter__()
#   __exit__()
#Cuando operamos sobre el objeto se llama al método __enter__() y cuando
#salimos, sea por el motivo que sea, se llama al método __exit__()

class with_test(object):
    
    def __init__(self, paramN):
        print ("En init...")
        self.n = paramN

    def __enter__(self):
        print ("En enter...")
        return(self)

    def __exit__(self, exc_type, exec_value, traceback):
        print ("Saliendo...")

    def metodo(self):
        print ("n vale: %s" % self.n)

with with_test(8) as wt:
    wt.metodo()
