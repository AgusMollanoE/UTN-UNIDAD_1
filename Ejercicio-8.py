# Ejercicio N°8

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

print("===================")
altura = float(input("Ingrese su altura en Metros: "))
peso = float(input("Ingrese su Peso en Kilos: "))

imc = peso / (altura * altura)

print(f"su Indice de Masa Corporal es : {imc:.2f}")