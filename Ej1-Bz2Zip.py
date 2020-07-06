import bz2

cadena = b"Cadena Cadena Cadena Cadena Cadena"

cadena_c = bz2.compress(cadena)

print("Cadena sin comprimir: ", cadena)

#Vemos la cadena comprimida pero no entendemos su contenido
print("Cadena comprimida: ", cadena_c)

#Si queremos visualizar el contenido original de la cadena comprimida
print(bz2.decompress(cadena_c))
    
