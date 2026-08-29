# Ejercicio N°1

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.


print("\nHola Mundo")

# Ejercicio N°2

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("\nBienvenido ingrese su Nombre: ")
print(f"Hola {nombre}")

# Ejercicio N°3

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#  imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#  “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#  años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#  la impresión por pantalla.

nombre = input("\nIngrese un Nombre: ")
apellido = input("Ingrese un Apellido: ")
edad = input("Ingrese una Edad: ")
residencia = input("Ingrese su lugar de recidencia: ")

print(f"Soy {nombre} {apellido}, y tengo {edad} años y vivo en {residencia}")

# Ejercicio N°4

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro

radio = int (input("\nIngrese el RADIO de un circulo: "))

area = (3.14 * (radio * radio))
perimetro = 2 * 3.14 * radio

print(f"El Area para el circulo de radio : {radio} es: {area:.2f} y su perimetro es: {perimetro:.2f}.")

# Ejercicio N°5

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("\nIngrese la cantidad de segundos a trasformar: "))

hora = segundos / 3600

print(f"con {segundos} segundos son {hora:.2f} horas.")

# Ejercicio N°6

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#  multiplicar de dicho número.

num = int(input("\nIngrese un numero para que se imprima una tabla de multiplicar: "))

print(f"1 x {num} = {num*1}")
print(f"2 x {num} = {num*2}")
print(f"3 x {num} = {num*3}")
print(f"4 x {num} = {num*4}")
print(f"5 x {num} = {num*5}")
print(f"6 x {num} = {num*6}")
print(f"7 x {num} = {num*7}")
print(f"8 x {num} = {num*8}")
print(f"9 x {num} = {num*9}")
print(f"10 x {num} = {num*10}")

# Se realizo de esta manera ya que se podria utilizar un For como contador pero esta unidad es solo
# de estructuras secuenciales.

# # Ejercicio N°7

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#  pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("\nIngrese su Primer Numero: "))
num2 = int(input("Ingrese otro Numero: "))

suma = num1 + num2
divicion = num1 / num2
multi = num1 * num2
resta = num1 - num2

print(f"la Suma de los Numeros {num1} + {num2} da como resultado: {suma}")
print(f"la Divicion de los Numeros {num1} / {num2} da como resultado: {divicion:.2f}")
print(f"la Multiplicacion de los Numeros {num1} X {num2} da como resultado: {multi}")
print(f"la Resta de los Numeros {num1} - {num2} da como resultado: {resta}")

# Ejercicio N°8

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

print("\n===================")
altura = float(input("Ingrese su altura en Metros: "))
peso = float(input("Ingrese su Peso en Kilos: "))

imc = peso / (altura * altura)

print(f"su Indice de Masa Corporal es : {imc:.2f}")

#Ejercicio N°9

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#    pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float (input("\nIngrese una Temperatura en Grados CELSIUS: "))

fahrenheit = ((9/5)* celsius) + 32

print(f"Su Equivalente en Fahrenheit es: {fahrenheit}")

# Ejercicio  N°10

#  10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#      dichos números.

num1 = int(input("\nIngrese su Primer Numero: "))
num2 = int(input("Ingrese au Segundo Numero: "))
num3 = int(input("Ingrese su Tercer Numero: "))

promedio= (num1 +  num2 + num3) / 3

print(f"El promedio fue: {promedio:.2f}")
