entrada = int(input())

listaFrases = []

for i in range(entrada):
    listaFrases.append(input())

respuesta = []
indicesAlreves = list(range(len(listaFrases)))
indicesAlreves.reverse()

for i in indicesAlreves:
    respuesta.append(listaFrases[i])


listaFrases.reverse()

for elemento in listaFrases:
    print(elemento)
