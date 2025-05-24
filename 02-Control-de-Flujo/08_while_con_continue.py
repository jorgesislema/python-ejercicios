"""
Ejercicio 8: while con continue

Objetivo: Usar continue para saltar iteraciones.

Instrucciones:
- Escribe un programa que muestre los números del 1 al 10, pero salte los múltiplos de 3.
"""

contador = 0
while contador < 10:
    contador += 1
    if contador % 3 == 0:
        continue
    print(contador)
