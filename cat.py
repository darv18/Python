import sys

def modoUso():
    print('Este escript junta los elementos que representan archivos de texto y los une')
    print('OPCIONES:')
    print('\t-o | --output: establece el archivo de salida')
    print('Ejemplo de uso:')
    print('\tpython cat.py --output /tmp/resultado.txt uno.txt dos.txt tres.txt')

def cat(listaArchivo, pathSalida):
    archivoSalida = open(pathSalida, 'w')
    for pathArchivo in listaArchivo:
        for linea in open(pathArchivo):
            archivoSalida.write(linea)
    archivoSalida.close()

if __name__ == '__main__':
    try:
        options, remainder = getopt.getopt(sys.agrv[1:], 'o:', ['output='])
        salida = ''
        for opcion, valor in options:
            if opcion in ('-o', '--output'):
                salida = valor

        if not salida or not remainder:
            raise Exception()
        cat(remainder, salida)
    except:
        modoUso()
