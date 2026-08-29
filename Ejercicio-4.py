# Ejercicio N°4

import math

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro

radio = int (input("Ingrese el RADIO de un circulo: "))

area = (math.pi * (radio * radio))
perimetro = 2 * math.pi * radio

print(f"El Area para el circulo de radio : {radio} es: {area:.2f} y su perimetro es: {perimetro:.2f}.")