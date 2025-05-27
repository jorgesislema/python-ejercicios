"""
Ejercicio 11: Multiprocessing básico

Objetivo: Crear y ejecutar un proceso usando multiprocessing.

Instrucciones:
- Escribe un programa que cree un proceso que imprima "Hola desde el proceso".
"""

from multiprocessing import Process

def saludar():
    print("Hola desde el proceso")

p = Process(target=saludar)
p.start()
p.join()
