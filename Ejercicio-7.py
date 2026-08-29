# Ejercicio N°7

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#  pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese su Primer Numero: "))
num2 = int(input("Ingrese otro Numero: "))

suma = num1 + num2
divicion = num1 / num2
multi = num1 * num2
resta = num1 - num2

print(f"la Suma de los Numeros {num1} + {num2} da como resultado: {suma}")
print(f"la Divicion de los Numeros {num1} / {num2} da como resultado: {divicion:.2f}")
print(f"la Multiplicacion de los Numeros {num1} X {num2} da como resultado: {multi}")
print(f"la Resta de los Numeros {num1} - {num2} da como resultado: {resta}")