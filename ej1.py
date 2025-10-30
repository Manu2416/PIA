Diccionario = {}

while (True):
    Palabra = input("dame una palabra para traducir")

    ListaPalabras = Palabra.split(";")

    for i in range(ListaPalabras):
        Diccionario[i] = ListaPalabras(i+1)

print (Diccionario)