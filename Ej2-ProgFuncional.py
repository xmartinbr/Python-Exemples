#Función de nivel superior
def saludo(idioma):
    def saludo_es():
        print("Hola")
    def saludo_en():
        print("Hello")

    idioma_func={"es":saludo_es,
                 "en":saludo_en
                }

    #Devuelve el nombre de la función a utilizar en fucnión del valor
    #del parámetro [idioma] pasado
    return idioma_func[idioma]

#saludar hace referencia al nombre de la función [saludo_es]
saludar = saludo("es")
#Al nombre de la función [saludo_es] se le añaden los parentesisis () y
#por lo tanto saludar() = saludo_es()
saludar()
#saludar hace referencia al nombre de la función [saludo_en]
saludar = saludo("en")
#Al nombre de la función [saludo_es] se le añaden los parentesisis () y
#por lo tanto saludar() = saludo_en()
saludar()
