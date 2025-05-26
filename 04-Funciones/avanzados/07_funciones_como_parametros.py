"""
Ejercicio 7: Funciones como parámetros

Objetivo: Comprender cómo pasar funciones como argumentos a otras funciones.

Instrucciones:
- Escribe una función que reciba otra función y una lista, y aplique la función a cada elemento de la lista.
- Prueba con funciones lambda y funciones definidas normalmente.
"""

def aplicar_funcion(func, lista):
    return [func(x) for x in lista]

# Ejemplo de uso
print(aplicar_funcion(lambda x: x * 2, [1, 2, 3, 4]))

def cuadrado(x):
    return x ** 2

print(aplicar_funcion(cuadrado, [1, 2, 3, 4]))
