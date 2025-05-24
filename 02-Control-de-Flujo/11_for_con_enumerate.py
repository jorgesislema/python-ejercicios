"""
Ejercicio 11: for con enumerate

Objetivo: Usar enumerate para obtener índices y valores.

Instrucciones:
- Escribe un programa que muestre los elementos de una lista junto con su índice.
"""

colores = ["rojo", "verde", "azul", "amarillo"]
for indice, color in enumerate(colores):
    print(f"Índice {indice}: {color}")
