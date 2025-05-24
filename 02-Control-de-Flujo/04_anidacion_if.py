"""
Ejercicio 4: Anidación de if

Objetivo: Practicar la anidación de estructuras condicionales.

Instrucciones:
- Escribe un programa que pida dos números y muestre cuál es mayor, o si son iguales.
"""

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

if a > b:
    print("El primer número es mayor.")
else:
    if a < b:
        print("El segundo número es mayor.")
    else:
        print("Ambos números son iguales.")
