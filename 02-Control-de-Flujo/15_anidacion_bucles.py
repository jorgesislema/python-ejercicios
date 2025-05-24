"""
Ejercicio 15: Anidación de bucles

Objetivo: Practicar bucles anidados.

Instrucciones:
- Escribe un programa que imprima una tabla de multiplicar del 1 al 5.
"""

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-")
