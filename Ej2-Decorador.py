#El parámetro [f] hace referencia a la dirección de memoria
# de la función [myAdd(a,b)]
def debug(f):
    print(f)
    #Función que añadirá funcionalidad a la función [myAdd()]
    #Los parámetros paramA y paramB en nuestro caso recibirán los
    #valores 7 y 5 que son los utilizados en la llamada de la función
    #[myAdd(7,5)].
    #Como se observa, les podemos cambiar el valor para que el resultado
    #final ya no sea sumar 7 + 5, sino (7+1) + (5+1)
    #Si deseamos que se continue ejecutando la función original entonces
    #deberemos retornar una llamada a la misma, en caso contrario no.
    #El parametro [*args] contien una tupla con todos los parámetros
    #que se han pasado
    def new_function(*args):
        print(f"New function {f.__name__}() called!")

        #Creamos otra tupla modificando los valores de la tupla original
        #pasada como parámetro
        argumentos = (5 + args[0], 10 + args[1])

        #En este caso no deseamos llamar a la función original y el resultado
        #mostrado será (7+1)*(5+1)=48
        #return paramA*paramB

        #En este caso si deseamos llamar a la función original y el resultado
        #mostrado será (7+1)+(5+1)=14.
        #En esta aituación el método devuelto debe tener la misma firma
        #que el método original
        return f(*argumentos)

        #Sino se realiza ningún return entonces sólo aparecerá el
        #mensaje por consola "Decorated function called!"

    #Como resultado del método que hace de decorador devolvemos un método
    #con la nueva funcionalidad
    return new_function


@debug
def myAdd(a, b):
    print("Original function myAdd() called!")
    return a + b

#Que sucede al utilitzar el decorador?
#Como la función myAdd(7,5) está decorada con el decorador @debug, en lugar
#de realizar la llamada a esta función en su lugar se hace la llamada al método
#cuyo nombre es igual al decorador y por lo tanto se llamará al método
#[debug(f)].
#Dentro de este método encontramos otro método [new_function(paramA, paramB)]
#que es donde definiremos la funcionalidad que queremos añadir a la función
#[myAdd()]. Si queremos que la función original [myAdd()] sea llamada entonces
#devolveremos la llamada a la función pasada por parámetro, sino simplemente
#no retornaremos nada.
print(myAdd(7,5))
