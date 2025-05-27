"""
Ejercicio 5: Hilos daemon

Objetivo: Comprender el uso de hilos daemon.

Instrucciones:
- Escribe un programa que cree un hilo daemon que imprima un mensaje cada segundo.
- El programa principal debe terminar después de 3 segundos.
"""

import threading
import time

def tarea():
    while True:
        print("Hilo daemon activo")
        time.sleep(1)

hilo = threading.Thread(target=tarea, daemon=True)
hilo.start()
time.sleep(3)
print("Programa principal terminado")
