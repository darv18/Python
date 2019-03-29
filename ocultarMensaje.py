import sys

def ocultarMensaje(imagen, salida, mensaje, step =2000):
    imagenOriginal = open(imagen, 'br')
    contenido = imagenOriginal.read()
    imagenOrginal.close()

    listaBytes = list(contenido)
    actual = step

    for letra in mensaje:
        byteAsoc = ord(letra)
        listaBytes[actual] = byteAsoc
        actual += step

    contenidoNUevo = bytes(listaBytes)
    arSalida = open(salida, 'wb')
    arSalida.write(contenidoNuevo)
    arSalida.close()


ocultarMensaje(sys.argv[1],sys.argv[2],sys.argv[3])
