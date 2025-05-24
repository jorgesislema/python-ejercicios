"""
Ejercicio 16: for anidado

Objetivo: Practicar bucles for anidados.

Instrucciones:
- Escribe un programa que imprima todas las combinaciones posibles de dos listas: colores y tallas.
"""

colores = ["rojo", "verde", "azul"]
tallas = ["S", "M", "L"]

for color in colores:
    for talla in tallas:
        print(f"{color} - {talla}")
