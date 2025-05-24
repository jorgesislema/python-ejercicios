"""
Ejercicio 12: for con break y continue

Objetivo: Practicar break y continue en bucles for.

Instrucciones:
- Escribe un programa que recorra una lista de números y muestre solo los positivos, deteniéndose si encuentra un cero.
"""

numeros = [3, 7, -2, 5, 0, 8, 4]
for n in numeros:
    if n == 0:
        break
    if n < 0:
        continue
    print(n)
