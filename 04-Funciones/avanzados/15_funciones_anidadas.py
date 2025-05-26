"""
Ejercicio 15: Funciones anidadas

Objetivo: Comprender el uso de funciones definidas dentro de otras funciones.

Instrucciones:
- Escribe una función que defina otra función dentro de sí misma y la utilice.
"""

def exterior(x):
    def interior(y):
        return x + y
    return interior

suma5 = exterior(5)
print(suma5(3))  # Imprime 8
