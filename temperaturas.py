from random import randint

mescontador = 1
temperaturas = []

def generartemperatura(n1, n2):
    global mescontador
    mes = [mescontador] 
    for i in range(30):
        temperatura = randint(n1, n2)
        mes.append(temperatura)
    temperaturas.append(mes)
    mescontador += 1  

while True:
    if 1 <= mescontador <= 3:
        generartemperatura(0, 18)
    elif 4 <= mescontador <= 6:
        generartemperatura(10, 25)
    elif 7 <= mescontador <= 9:
        generartemperatura(22, 40)
    elif 10 <= mescontador <= 12:
        generartemperatura(15, 28)
    else:
        break

print(temperaturas)

with open("temperaturas1.txt", "a", encoding="utf-8") as f:
    for lista in temperaturas:
        f.write("\n")  
        for i in range(len(lista)):
            f.write(str(lista[i]))
            if i != len(lista) - 1:  
                f.write(",")
import matplotlib.pyplot as plt

# Leer archivo
meses = []

with open("temperaturas1.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    linea = linea.strip()  # quitar salto de línea
    if linea:               # ignorar líneas vacías
        mes = []            # crear lista nueva para cada mes
        for n in linea.split(","):
            mes.append(int(n))  # convertir a entero
        meses.append(mes)

print(meses)  # cada sublista es un mes completo

# Graficar
plt.figure(figsize=(12, 6))

for mes in meses:
    numero_mes = mes[0]       # primer número = número del mes
    temperaturas = mes[1:]    # siguientes 30 números = temperaturas
    plt.plot(range(1, 31), temperaturas, label=f"Mes {numero_mes}")

plt.xlabel("Día del mes")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas diarias por mes")
plt.legend()
plt.grid(True)
plt.show()