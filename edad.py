dia = int(input())
mes = int(input())
año = int(input())

if mes >= 3:
    a = 1
elif mes < 3:
    a = 0

if dia >= 12:
    a = 1
elif dia < 12:
    a = 0

if año < 2019:
    resultado = 2019 - año
    print(resultado - a)
elif año >= 2019:
    resultado = 2019 - año
    print(resultado + 1)
