"""
Ejercicio 4: Pausa en hilos

Objetivo: Usar time.sleep en hilos.

Instrucciones:
- Escribe un programa que cree un hilo que imprima un mensaje, espere 2 segundos y luego imprima otro mensaje.
"""

import threading
import time

def tarea():
    print("Inicio de la tarea")
    time.sleep(2)
    print("Fin de la tarea")

hilo = threading.Thread(target=tarea)
hilo.start()
hilo.join()
