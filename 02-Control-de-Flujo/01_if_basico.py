"""
Ejercicio 1: Uso básico de if

Objetivo: Comprender la estructura condicional if en Python.

Instrucciones:
- Escribe un programa que pida al usuario un número y muestre si es positivo, negativo o cero.
"""

numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
