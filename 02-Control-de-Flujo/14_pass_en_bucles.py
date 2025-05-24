"""
Ejercicio 14: Uso de pass en bucles

Objetivo: Comprender el uso de pass como instrucción nula.

Instrucciones:
- Escribe un programa que recorra una lista y use pass para los elementos negativos.
"""

numeros = [2, -1, 4, -3, 6]
for n in numeros:
    if n < 0:
        pass  # No hacer nada con negativos
    else:
        print(n)
