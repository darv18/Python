import zipfile
import crypt
import sys

archivo = '/home/daniel/Documentos/Python/reto.zip' #El archivo que quiero Descomprimir
diccionario = '/home/daniel/Documentos/Python/listado-general.txt'
comprimido = zipfile.ZipFile(archivo)

for palabra in open(diccionario):
    try:
        limpia = palabra.strip()
        comprimido.extractall(path='archivo',pwd=bytes(limpia.encode('utf-8')))
        print('La clave es: %s' % limpia)
    except:
        pass
        #print('Clave valida')
