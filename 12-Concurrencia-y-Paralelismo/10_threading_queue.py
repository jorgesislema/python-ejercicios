"""
Ejercicio 10: Uso de Queue

Objetivo: Compartir datos entre hilos usando queue.Queue.

Instrucciones:
- Escribe un programa donde un hilo productor ponga datos en una cola y un hilo consumidor los saque e imprima.
"""

import threading
import queue
import time

q = queue.Queue()

def productor():
    for i in range(5):
        print(f"Produciendo {i}")
        q.put(i)
        time.sleep(0.5)
    q.put(None)  # Señal de fin

def consumidor():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumiendo {item}")

h1 = threading.Thread(target=productor)
h2 = threading.Thread(target=consumidor)
h1.start()
h2.start()
h1.join()
h2.join()
