import tarfile

archivo_tar = tarfile.open('primer.tar.gz','w:gz')

archivo_tar.add('Ej2-Clases.py')
archivo_tar.add('Ej1-Clases.py')
archivo_tar.close()


    
