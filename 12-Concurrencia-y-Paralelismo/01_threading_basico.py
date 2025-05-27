"""
Ejercicio 1: Threading básico

Objetivo: Crear y ejecutar un hilo simple en Python.

Instrucciones:
- Escribe un programa que cree un hilo que imprima "Hola desde el hilo".
"""

import threading

def saludar():
    print("Hola desde el hilo")

hilo = threading.Thread(target=saludar)
hilo.start()
hilo.join()
