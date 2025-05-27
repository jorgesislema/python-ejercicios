"""
Ejercicio 3: Hilos con argumentos

Objetivo: Pasar argumentos a funciones ejecutadas en hilos.

Instrucciones:
- Escribe un programa que cree un hilo que reciba un nombre y lo imprima.
"""

import threading

def saludar(nombre):
    print(f"Hola, {nombre}!")

hilo = threading.Thread(target=saludar, args=("Pythonista",))
hilo.start()
hilo.join()
