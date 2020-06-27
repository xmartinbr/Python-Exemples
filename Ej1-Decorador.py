#*args -> tupla de parametros sin nombre
#*kwargs -> diccionario de parametros con nombre
#Se utilizan uno u el otro o los 2 a la vez cuando se desconoce la cantidad
#de parametros que se pasarán a la función.
#Siempre se colocan como parámetros finales en la función, ej:
#   funcion(paramA,paramB,*args,**kwargs)
#   funcionA(*args,**kwargs)
def primerD(paramFunc):      
    def funcionDecorada(*args,**kwargs):
        print("Funcion decorada")
    return (funcionDecorada)


#Hacemos referencia al decorador, el nombre debe coincidir
#con el del método que se dese decorar. En este caso lo que estamos
#haciendo es modificar el comportamiento de la función (funcionA()), o sea le
#indicamos a Python que al llamar a la función (funcionA()) no la ejecute
#y en su lugar ejecute la función (primerD(funcion))
#El decorador debe de ser un objeto llamable y por lo tanto si se ha declarado
#como una clase deberá implementar el método __call__
@primerD
def funcionA(val1,val2):
    print('Mi 1º decorador')

funcionA(2,3)


#http://www.3engine.net/wp/2015/02/decoradores-python/
#http://www.3engine.net/wp/2015/09/decoradores-python-con-parametros/
