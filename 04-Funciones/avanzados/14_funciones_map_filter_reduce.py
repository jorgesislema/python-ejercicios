"""
Ejercicio 14: map, filter y reduce

Objetivo: Practicar el uso de funciones de orden superior map, filter y reduce.

Instrucciones:
- Usa map para elevar al cuadrado una lista de números.
- Usa filter para quedarte solo con los pares.
- Usa reduce para sumar todos los elementos.
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]
cuadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
suma = reduce(lambda x, y: x + y, numeros)

print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Suma:", suma)
