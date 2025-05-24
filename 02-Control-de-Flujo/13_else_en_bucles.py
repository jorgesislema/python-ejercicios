"""
Ejercicio 13: else en bucles

Objetivo: Comprender el uso de else con bucles.

Instrucciones:
- Escribe un programa que busque un número en una lista y muestre si lo encontró o no usando else con el bucle.
"""

numeros = [1, 3, 5, 7, 9]
buscar = int(input("¿Qué número quieres buscar?: "))

for n in numeros:
    if n == buscar:
        print("¡Encontrado!")
        break
else:
    print("No encontrado.")
