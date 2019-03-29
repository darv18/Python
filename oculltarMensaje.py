"""
Este escrypt recvibe una imagen, un mesaje y una ruta de salida
guarda el mensaje en la imagen de salida

"""

import sys

def ocultarmensaje(pathimagen, mensaje, pathsalida, skip=1000):
    imagenOriginal = open(pathimagen, 'br')
    contenido = imagenOriginal.read()
    listaBytes = list(contenido)
    actual = skip
    for caracter in mensaje:
        listaBytes[actual] = ord(caracter)
        actual += skip
    resultado = bytes(listaBytes)
    salida = open(pathsalida, 'wb')
    salida.write(resultado)
    salida.close()


ocultarmensaje(sys.argv[1],sys.argv[2],sys.argv[3])
