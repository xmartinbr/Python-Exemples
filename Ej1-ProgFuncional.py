def lower(elementos): return elementos.lower()

lista = ["JOSE","ANDREs","No"]

print(list(map(lower,lista)))
print(list(map(lambda x: x.lower(),lista)))

#Sin utilizar map()
print([cad.lower() for cad in lista])
