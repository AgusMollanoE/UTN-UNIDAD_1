# Ejercicio 

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#  imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#  “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#  años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#  la impresión por pantalla.

nombre = input("Ingrese un Nombre: ")
apellido = input("Ingrese un Apellido: ")
edad = input("Ingrese una Edad: ")
residencia = input("Ingrese su lugar de recidencia: ")

print(f"Soy {nombre} {apellido}, y tengo {edad} años y vivo en {residencia}")