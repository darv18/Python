tamano = int(input())
lista = []

for i in range(tamano):

    lista.append(input())

    if tamano % 2 == 0: #tamaño par
        hasta = tamano // 2
        lista = lista[:hasta-1] + lista[hasta+1]

    else:
        lista = lista[:len(lista)//2] + lista[(len(lista)//2)+1:]

for elemento in lista:
    print(elemento)

