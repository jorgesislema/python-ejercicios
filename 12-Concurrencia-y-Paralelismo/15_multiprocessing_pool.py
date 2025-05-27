"""
Ejercicio 15: Pool de procesos

Objetivo: Ejecutar tareas en paralelo usando multiprocessing.Pool.

Instrucciones:
- Escribe un programa que use un Pool para calcular los cuadrados de una lista de números en paralelo.
"""

from multiprocessing import Pool

def cuadrado(x):
    return x * x

with Pool(4) as pool:
    resultados = pool.map(cuadrado, [1, 2, 3, 4, 5])
print(resultados)
