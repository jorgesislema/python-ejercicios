"""
Ejercicio 9: Funciones con *args y **kwargs avanzados

Objetivo: Profundizar en el uso de argumentos variables.

Instrucciones:
- Escribe una función que acepte cualquier cantidad de argumentos posicionales y de palabra clave, y los imprima de forma ordenada.
"""

def mostrar_argumentos(*args, **kwargs):
    print("Posicionales:", args)
    print("Palabra clave:", kwargs)

mostrar_argumentos(1, 2, 3, a=10, b=20)
