"""
Ejercicio 7: Uso de RLock

Objetivo: Comprender el uso de threading.RLock para reentrancia.

Instrucciones:
- Escribe un programa que use un RLock para permitir que un hilo adquiera el mismo lock varias veces.
"""

import threading

rlock = threading.RLock()

def tarea():
    with rlock:
        print("Primer nivel de bloqueo")
        with rlock:
            print("Segundo nivel de bloqueo")

hilo = threading.Thread(target=tarea)
hilo.start()
hilo.join()
