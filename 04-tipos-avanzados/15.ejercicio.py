# 1. Funcion para eliminar los espacios de un stris
# y devolver una lista con los caraceres restantes
def eliminar_Espacio(texto):
    return list(texto.replace(" ", ""))


# 2. Contar en un diccionario cuanto se repiten los caractares de un string
def contar_caracteres(texto):
    texto = eliminar_Espacio(texto)
    lista = {}
    for caracter in texto:
        if caracter not in lista:
            lista[caracter] = 1
        else:
            lista[caracter] += 1
    return lista

# 3 Ordernar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas [("a",3),("b",2),("c",4)]


def ordenar_llaves(dicc):
    lista = []
    for elemento in dicc:
        lista.append(tuple([elemento, dicc[elemento]]))
    return (lista)

# 4. De un listado de tuplas devolver la tuplas que tengan el mayor valor. [("a",3),("b",2),("c",4),("s",4)] → [("s",4),("c",4),"a",3),("b",2)]


def tuplas_mayor_valor(lista_tuplas):
    lista_tuplas.sort(key=lambda elemento: elemento[1], reverse=True)
    return lista_tuplas

# 5. Crear un mensaje que diga:
# Los caracteres que más se repirte con {números} repeticiones son → una lista
# o lista con los caraceteres que más se hayan repetidos y el caracter en mayusculas

# 6 Juntar la solución de los ejercicios anteriores para encontar los caracteres que más se repiten de un string


def mensaje(lista_tuplas):
    i = 0
    dicc = {}
    while (i < len(lista_tuplas)-1):
        valor_max = lista_tuplas[i][1]
        if (lista_tuplas[i][1] == lista_tuplas[i+1][1]):
            dicc[(lista_tuplas[i][0]).upper()] = lista_tuplas[i][1]
            dicc[(lista_tuplas[i+1][0]).upper()] = lista_tuplas[i+1][1]
        else:
            dicc[(lista_tuplas[i][0]).upper()] = lista_tuplas[i][1]
            break
        i += 1

    print(
        f"los caracteres que más se repinten con {valor_max} repeticiones y son")

    for elemento in dicc:
        print(elemento)

# Función que una todo


def union_all(mi_string):
    a = contar_caracteres(mi_string)
    b = ordenar_llaves(a)
    c = tuplas_mayor_valor(b)
    mensaje(c)


union_all("Hola mundo este es mi string")
