numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if numero1 < numero2 and numero1 < numero3:
    print(numero1)

elif numero2 < numero1 and numero2 < numero3:
    print(numero2)

elif numero3 < numero1 and numero3 < numero2:
    print(numero3)
