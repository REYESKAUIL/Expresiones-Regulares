import re
Opcion=0

while Opcion != 11: 
    print('°°°°°°°°°°°°°°°°°°°°*Expresiones Regulares*°°°°°°°°°°°°°°°°°°°')
    print('\nSELECCIONA UNA OPCION')
    print('1.Todas las palabras que tengan una longitud de 7 o mas letras')
    print('2.Expresiones que NO finalicen con una vocal')
    print('3.Las palabras que inicien con "M" donde la segunda letra no sea vocal')
    print('4.Expresiones encerradas entre comillas')
    print('5.Ip´s')
    print('6.Horas')
    print('7.Telefonos')
    print('8.Correos electronicos')
    print('9.Url´s')
    print('10.Codigo postal')
    Opcion = int(input("Opción a realizar: "))

    if Opcion == 1:
        print('Resultado de la busqueda')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "[a-zA-Z]{7,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif Opcion == 2:
        print('Resultado de la busqueda')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = "[A-Za-z]+[^aeiou]$"
            for elemento in lista:
                if re.search(regex,elemento):
                   print(elemento)
        textfile.close()  

    elif Opcion == 3:
        print('Resultado de la busqueda')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "([M][^aeiou][a-zA-z]+)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close() 

    elif Opcion == 4:
        print('Resultado de la busqueda')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "(\".*\")"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif Opcion == 5:
        print('Resultado de la busqueda de Ip´s')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "([0-9]{0,3}[\.]+[0-9]{0,3}[\.]+[0-9]{0,3}[\.]+[0-9]{0,3})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif Opcion == 6:
        print('Resultado de la busqueda de Horas')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "([0-9]{0,2}\:[0-9]{2})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif Opcion == 7:
        print('Resultado de la busqueda de Telefonos')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "([0-9]{10})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif Opcion == 8:
        print('Resultado de la busqueda de Correos electronicos')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "([a-zA-z]{0,}\@[a-zA-z]{0,}\.[a-zA-z]{0,})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif Opcion == 9:
        print('Resultado de la busqueda de Url’s')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "([a-zA-Z]{0,}\:[\/][\/]+[a-zA-Z0-9].*\.[a-zA-Z0-9].*\.[a-zA-Z].*\/[a-zA-Z].*\/[a-zA-Z0-9].*\?[a-zA-Z].*\=[a-zA-Z]{0,})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif Opcion == 10:
        print('Resultado de la busqueda de Codigos postales')
        filename = "Texto_Informativo.txt"
        textfile = open(filename, "r")
        regex = "[0-9]{5}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()  

    else:
        print('Solo permite el ingreso de valores de las opciones indicadas')

        print('°°°°°°°°°°°°°°°°°°°°*Gracias*°°°°°°°°°°°°°°°°°°°')