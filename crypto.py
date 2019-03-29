import sys
import cryp

def recuperarHash(usuario, archivoPass):
    for linea in open(archivoPass):
        if linea.startswith(usuario):
            # procesar esa linea
            partes = linea.split(':')
            return partes[1]
 
 
def crackearPass(usuario, archivoPass, archivoDiccionario):
    miHash = recuperarHash(usuario, archivoPass)
    salt = miHash[:2]
    for palabra in open(archivoDiccionario):
        limpia = palabra.strip()
        otroHash = crypt.crypt(palabra, salt)
        if otroHash == miHash:
            return palabra
 
if __name__ == '__main__':
 
    if len(sys.argv) != 4:
        print('Debes pasar el usuario, el path de passw y el path del diccionario')
        exit(1)
         
         
    print(crackearPass(sys.argv[1], sys.argv[2], sys.argv[3]))
