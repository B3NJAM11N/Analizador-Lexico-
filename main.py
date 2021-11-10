#Autor Miguel Benjamin Perez Suasnavar
# Materia: Lenguajes y Automatas I
# Docente: Jose Leonel Pech May
# 5to B ISC

import re

opcion = 0
while opcion != 6:
    print("\nEscoja una opcion")
    print(
        "1.variables validas\n2.Enteros y decimales\n3.Expresiones aritmeticas\n4.operadores condicionales\n5.cadena de carateres\n6.salir ")
    opcion = int(input("ingresa una opcion"))

    if opcion == 1:
        print("variables validas Ejem: suma,i,cont7.")
        filename = "EjerciciosT4.txt"
        textfile = open(filename, "r")
        regex = "double\s[a-z]+|int\s[a-z]+|String\s[a-z]+|long\s[a-z]+|boolean\s[a-z]+"
        reg = re.compile(regex)
        print("--------------------------------------------")
        for line in textfile:
            lista = reg.findall(line)
            for i in range(0, len(lista)):
                print(lista[i])

        textfile.close()
        print("--------------------------------------------")

    elif opcion == 2:
        print("Enteros y decimales Ejem: 2.7, 3.1416")
        filename = "EjerciciosT4.txt"
        textfile = open(filename, "r")
        regex = "\d+\.+\d+|\d+"
        reg = re.compile(regex)
        print("--------------------------------------------")
        for line in textfile:
            lista = reg.findall(line)
            for i in range(0, len(lista)):
                print(lista[i])

        print("--------------------------------------------")

    elif opcion == 3:
        print("expresiones aritmeticas Ejemp: suma=2+1, cont=cont+1")
        filename = "EjerciciosT4.txt"
        textfile = open(filename, "r")
        regex = "[a-zA-Z]+\s*=+\s*[a-zA-Z0-9]+\s*[\-\*\+\/]+\s*[a-zA-Z0-9]+"
        reg = re.compile(regex)
        print("--------------------------------------------")
        print("\n")
        for line in textfile:
            lista = reg.findall(line)
            for i in range(0, len(lista)):
                print(lista[i])

        textfile.close()
        print("--------------------------------------------")

    elif opcion == 4:
        print("operadores condicionales Ejemp: edad>=18, cont<100")
        filename = "EjerciciosT4.txt"
        textfile = open(filename, "r")
        regex = "[a-z0-9]+\s*[<>=!]+\s*[a-z0-9]+"
        reg = re.compile(regex)
        print("--------------------------------------------")
        for line in textfile:
            lista = reg.findall(line)
            for i in range(0, len(lista)):
                print(lista[i])
        print("--------------------------------------------")

    elif opcion == 5:
        print("Cadena de caracteres")
        filename = "EjerciciosT4.txt"
        textfile = open(filename, "r")
        regex = "[\"]+.*[\"]+"
        reg = re.compile(regex)
        print("--------------------------------------------")
        for line in textfile:
            lista = reg.findall(line)
            for i in range(0, len(lista)):
                print(lista[i])
        textfile.close()
        print("--------------------------------------------")
    else:
        print("opcion incorrecta")
