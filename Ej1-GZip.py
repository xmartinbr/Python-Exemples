import gzip

#Abrimos el fichero .pdf que deseamos comprimir
#Cuando indicamos el nombre del fichero que contendrá el fichero original
#comprimido, este debe seguir un patrón:
#   [nombre del archivo].[extensión del fichero a comprimir].[gz]
#Sino indicamos la extensión del fichero original, al descomprimir se creará
#el fichero resultante con la extensión aquí indicada. Para poder entonces
#abrirlo con su programa por mdefecto préviamente deberemos modificar la
#extensión manualmente.
with open('D:\\ReaderBooks\\epdf.pub_english-grammar-in-use.pdf','rb') as original:
    with gzip.open('D:\\ReaderBooks\\archivo.pdf.gz','wb') as archivo1:
        archivo1.writelines(original)
    
