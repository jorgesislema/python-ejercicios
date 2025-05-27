"""
Ejercicio 9: Uso de Semaphore

Objetivo: Limitar el acceso concurrente a un recurso con threading.Semaphore.

Instrucciones:
- Escribe un programa donde solo 3 hilos puedan acceder simultáneamente a una sección crítica.
"""

import threading
import time

semaforo = threading.Semaphore(3)

def tarea(n):
    with semaforo:
        print(f"Hilo {n} accediendo a la sección crítica")
        time.sleep(1)
        print(f"Hilo {n} saliendo")

hilos = [threading.Thread(target=tarea, args=(i,)) for i in range(6)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()
