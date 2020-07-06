import zipfile
from zipfile import ZipFile

#Creamos un fichero .zip que contendrá otros 2 ficheros ya comprimidos
with zipfile.ZipFile('D:\\ReaderBooks\\archivo.zip', 'a') as fzip:
    fzip.write('D:\\ReaderBooks\\epdf.pub_english-grammar-in-use.pdf')
    fzip.write('D:\\ReaderBooks\\DSC_0121.jpg')
    fzip.printdir()
    
