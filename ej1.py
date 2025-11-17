import csv

def procesar_ventas(fichero,productos_buscar):
    listas = []
    cantidad_productos = 0
    mismo_producto = 0
    with open(fichero,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            listas.append(row)

    for lista in listas:
        for i in range(len(lista)):
            if lista[i] == productos_buscar:
                    mismo_producto += 1
                    cantidad_productos += int(lista[1])
                    beneficio = cantidad_productos * int(lista[2])
                    return ( f" el producto {productos_buscar} ha obtenido un beneficio de {beneficio} {mismo_producto}")
            else:
                 return ("No existe ese productos")
                    
        
    

procesar_ventas("./docsEJ/productos.csv","hig")