import re

#El método [search()] retorna un obj. de tipo [Match]
#Obtenemos la pos. donde se encuentra la 1ª "k"
print(re.search(r"k","kilometrok"))

#Obtenemos la pos. donde se encuentran los primeros 3 dígitos
#Sino encuentra 3 dígitos devolverá None
print(re.search(r"\d\d\d","kilo912metr123o"))

#Creamos el patrón de búsqueda
patron = re.compile(r'\d\d\d')
#El método [group()] del obj. de tipo Match devuelto por el método [search()]
#devuelve la parte de la cadena donde se ha encontrado la coincidencia.
#Sino encuentra 3 dígitos lanzará una exception
print(patron.search("kilometr132o").group())

# \Aa   : la cadena debe empezar por 'a'
# [0-9] : el siguiente char. debe ser un dígito entre el 0 y el 9
# .*    : cualquier char. excepto el de nueva línea con 0 o más ocurrencias.
# (end|fin) : la cadena debe contener la palabra 'end' o 'fin'
# .$        : la cadena debe finalizar en '.'
#Si el patrón no se encuentra no devuelve nada
if (re.search(r"\Aa[0-9].*(end|fin).$","a4 es una marca de fin.")):
    print("Se encontro el patron")

#Buscamos en la cadena el patrón "\d", o sea un dígito y cuando lo encuentra
#lo sustituye por un '*'
print(re.sub(r"\d","*","mpang8uera990"))

#Buscamos en la cadena el patrón "\d", o sea un dígito y cuando lo encuentra
#lo sustituye por un '*', pero sólo aplica en los 2 primeros números encontrados
print(re.sub(r"\d","*","mpang8uera990",2))

#re.IGNORECASE es un modificador que le indica a Python que aunque en el
#patrón se indique "ab" minúsculas también coincidirán con el patrón "AB"
#mayúsculas y por lo tanto el conjunto que se estará buscando es
# {(a,b),(A,B),(A,b),(a,B)}
regex = re.compile(r"ab",re.IGNORECASE)

print(regex.search("jutnmilajaBuimnhtr"))

